import sqlite3
from bottle import route, run, debug, template, request, static_file, error

@route('/all')
def all():
    conn = sqlite3.connect('animals.db')
    c = conn.cursor()
    c.execute("SELECT * FROM animals")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new', method='GET')
def new_item():

    if request.GET.save:
        new_name = request.GET.name.strip()
        new_type = request.GET.type.strip()

        conn = sqlite3.connect('animals.db')
        c = conn.cursor()

        c.execute("INSERT INTO animals (name,type) VALUES (?,?)", (new_name, new_type))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new name was inserted into the database, the ID is %s</p>' % new_id

    else:
        return template('new_name.tpl')


@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.name.strip()
        type = request.GET.type.strip()

        conn = sqlite3.connect('animals.db')
        c = conn.cursor()
        c.execute("UPDATE animals SET name = ?, type = ? WHERE id LIKE ?", (edit, type, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('animals.db')
        c = conn.cursor()
        c.execute("SELECT name FROM animals WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_name', old=cur_data, no=no)


run(reloader=True, debug=True, port=8000)
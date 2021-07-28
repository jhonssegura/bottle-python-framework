%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the name with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  
  <p>Escriba el nombre</p>
  <input type="text" name="name" value="{{old[0]}}" size="20" maxlength="20">
  <p>Escriba el tipo</p>
  <input type="text" name="type" value="{{old[0]}}" size="20" maxlength="20">
  <br>
  <input type="submit" name="save" value="save">
</form>
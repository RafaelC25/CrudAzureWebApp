document.addEventListener("DOMContentLoaded", search);
const URL_API = 'http://localhost:3000/api/'

var employees = []

function init() {
    search()
}

function agregar(){
    clean()
    abrirFormulario()
}

function abrirFormulario(){
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class","modale opened")
}
function cerrarModal(){
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class","modale")
}


async function search() {
    var url = URL_API + 'employee'
    var response = await fetch(url, {
        "method": 'GET',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    employees = await response.json();

    var html = ''
    for(employee of employees){
    var row = `<tr>
    <td>${employee.firstname}</td>
    <td>${employee.lastname}</td>
    <td>${employee.email}</td>
    <td>${employee.address}</td>
    <td>
        <button onclick="remove(${employee.id})" class="btn">Eliminar</button>
        <button onclick="edit(${employee.id})" class="btn">Editar</button>
    </td>
</tr>`
        html = html + row;
    }
    

    document.querySelector('#customers > tbody').outerHTML = html
}

function edit(id){
    abrirFormulario()
    var employee = employees.find(x => x.id == id)
    document.getElementById('txtId').value = employee.id
    document.getElementById('txtAddress').value = employee.address
    document.getElementById('txtFirstname').value = employee.firstname
    document.getElementById('txtLastname').value = employee.lastname
    document.getElementById('txtEmail').value = employee.email
}

async function remove(id){
   respuesta = confirm('Desea eliminar este empleado?')
   if (respuesta){
    var url = URL_API + 'employee/' + id
    await fetch(url, {
        "method": 'DELETE',
        "headers": {
            "Content-Type": 'application/json'
        }
    })
    window.location.reload();
   }
}

function clean(){
    document.getElementById('txtId').value = ''
    document.getElementById('txtAddress').value = ''
    document.getElementById('txtFirstname').value = ''
    document.getElementById('txtLastname').value = ''
    document.getElementById('txtEmail').value = ''
}

async function save() {
    var data = {
      "address": document.getElementById('txtAddress').value,
      "email": document.getElementById('txtEmail').value,
      "firstname": document.getElementById('txtFirstname').value,
      "lastname": document.getElementById('txtLastname').value,
    }
  
    var id = document.getElementById('txtId').value
    if (id != ''){
        data.id = id
    }
    var url = URL_API + 'employees'
    await fetch(url, {
      "method": 'POST',
      "body": JSON.stringify(data),
      "headers": {
      "Content-Type": 'application/json'
      }
    })
    window.location.reload();
  }
@startuml

class Persona {
  codigo: string
  nombres : string
}

class Empleado {
   fechaIngreso : Date
   sueldo : Float
}

class RepositorioEmpleado {
    empleados : List

    + buscar(codigo): empleado
    + agregar (empleado) : boolean
    + editar (empleado) : boolean
    + eliminar (empleado) : boolean
}

class CasoUsoEmpleado{
    empleado : object
    repositorioEmpleado: object

    void constructor(repositorioEmpleado)
    + buscar(codigo): empleado
    + agregar (empleado) : boolean
    + editar (empleado) : boolean
    + eliminar (empleado) : boolean


}


Persona <|-- Empleado
RepositorioEmpleado *-- CasoUsoEmpleado
@enduml
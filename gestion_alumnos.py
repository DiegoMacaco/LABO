import json# Importamos nuestro archivo Json 

def cargar_alumnos(ruta_archivo):# creando la funcion para cargar los datos de los alumnos 
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

def buscar_alumno(alumnos, nombre):# creando la funcion para cargar los datos de los alumnos 
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():# Buscar con mayusculas o minusculas 
            return alumno
    return None


if __name__ == "__main__": # hacer correr nuestro archivo
    ruta = "LABO/alumnos.json" # ruta de archivo JSON
    alumnos = cargar_alumnos(ruta) 
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")

    resultado = buscar_alumno(alumnos, nombre_buscar)
    if resultado:# if por falso o verdadero
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")
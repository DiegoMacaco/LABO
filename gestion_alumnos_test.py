import unittest 
from gestion_alumnos import buscar_alumno # Del archivo se importa su metodo de buscar alumno 

class TestGestionAlumnos(unittest.TestCase): # Clase del archivo Json 

    def setUp(self): # Funcion de la clase  TestGestionAlumnos
        self.alumnos = [
            {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
            {"nombre": "Luis", "edad": 22, "carrera": "Matemáticas"},
            {"nombre": "María", "edad": 21, "carrera": "Física"} # Datos para verificar si hay errores 
        ]

    def test_buscar_alumno_existente(self): # Buscador de errores 
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Ana")# Buscador de errores 

    def test_buscar_alumno_inexistente(self): # Buscador de errores 
        resultado = buscar_alumno(self.alumnos, "Carlos")# Buscador de errores 
        self.assertIsNone(resultado)

if __name__ == "__main__": # metodo principal
    unittest.main()
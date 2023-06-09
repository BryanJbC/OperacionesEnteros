import unittest
from src.logica.OperacionesEnteras import OperacionesEnteros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCD_dosNumerosPositivos_retornaMCD(self):
         # Arrange
         numero1 = 18
         numero2 = 24
         resultadoEsperado = 6
         operacion = OperacionesEnteros([numero1, numero2])

         # Do
         resultadoActual = operacion.calcularMCD()

         # Assert
         self.assertEqual(resultadoEsperado, resultadoActual)
    def test_MCD_tresNumerosPositivos_retornaMCD(self):
         # Arrange
         numero1 = 24679
         numero2 = 20387
         numero3 = 16169
         resultadoEsperado = 37
         operacion = OperacionesEnteros([numero1, numero2, numero3])

         # Do
         resultadoActual = operacion.calcularMCD()

         # Assert
         self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCD_cuatroNumerosPositivos_retornaMCD(self):
        # Arrange
        numero1 = 4
        numero2 = 6
        numero3 = 14
        numero4 = 10
        resultadoEsperado = 2
        operacion = OperacionesEnteros([numero1, numero2, numero3, numero4])

        # Do
        resultadoActual = operacion.calcularMCD()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)






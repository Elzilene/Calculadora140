# 1 - bibliotecas, framwworks e referências externas
import pytest # framework de teste de unidade

# funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2 - tests
def test_somar_dois_numeros():

# Padrão / Stardard  AAA(se diz triple A/ 3A)= Arrange, Act, Assert
    # Prepara/ configura
    # Dados de entrada e saida
    num1 = 5
    num2 = 7
    resultado_esperado = 12 

    # Act / executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido





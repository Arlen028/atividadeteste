import unittest

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return round(a / b, 2)

def media(lista):
    return sum(lista) / len(lista)

def maiorvalor(lista):
    return max(lista)

def menorvalor(lista):
    return min(lista)

def numeroprimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def parouimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def funcao_exemplo(x):
    return x ** 2

def outra_funcao_exemplo(x, y):
    return x + y

# Testes unitários
class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(3, 5), 8)
        self.assertEqual(soma(-3, 5), 2)
    
    def test_subtracao(self):
        self.assertEqual(subtracao(8, 5), 3)
        self.assertEqual(subtracao(3, 5), -2)
    
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 5), 15)
        self.assertEqual(multiplicacao(-3, 5), -15)
    
    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5.0)
        self.assertEqual(divisao(7, 3), 2.33)

    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(media([10, 20, 30, 40, 50]), 30.0)

    def test_maiorvalor(self):
        self.assertEqual(maiorvalor([1, 3, 5, 7, 9]), 9)
        self.assertEqual(maiorvalor([-1, -3, -5, -7, -9]), -1)

    def test_menorvalor(self):
        self.assertEqual(menorvalor([1, 3, 5, 7, 9]), 1)
        self.assertEqual(menorvalor([-1, -3, -5, -7, -9]), -9)

    def test_numeroprimo(self):
        self.assertTrue(numeroprimo(2))
        self.assertTrue(numeroprimo(7))
        self.assertFalse(numeroprimo(4))
        self.assertFalse(numeroprimo(9))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_parouimpar(self):
        self.assertEqual(parouimpar(10), "Par")
        self.assertEqual(parouimpar(7), "Ímpar")
    
    def test_funcao_exemplo(self):
        self.assertEqual(funcao_exemplo(4), 16)
    
    def test_outra_funcao_exemplo(self):
        self.assertEqual(outra_funcao_exemplo(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
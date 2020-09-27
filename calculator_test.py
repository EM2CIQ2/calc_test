import unittest
from calculator import *

class CalculatorTest(unittest.TestCase):

    '''
    Test akan mengecheck String result dan expected
    '''
    def test_output(self):
        self.assertEquals(self.calc.what, "Calculator adalah kelas yang memiliki fungsi perhitungan")

    '''
    Test akan mengecheck hasil pertambahan
    '''
    def test_add_same(self):
        self.assertEqual(self.calc.add(5,5), 10)

    '''
    Test akan mengecheck kesalahan
    bahwa hasil bukan Float
    '''
    def test_false(self):
        self.assertFalse(isinstance(self.calc.add(5,5), float))

    '''
    Test akan mengecheck kebenaran
    bahwa hasil adalah int
    '''
    def test_true(self):
        self.assertTrue(isinstance(self.calc.add(5,5), int))

    '''
    Test mengecheck bahwa calc
    adalah instance dari calculator
    '''
    def test_is_it(self):
        self.assertIsInstance(self.calc, calculator)

    '''
    Test akan mengecheck pembagian 0
    dengan hasil dari fungsi dari Kelas
    '''
    def test_division_zero_a(self):
        result = self.calc.division(0, 0)
        self.assertFalse(result[1])

    '''
    Test akan mengecheck pembagian dengan hasil infinity
    dengan hasil dari fungsi dari Kelas
    '''
    def test_division_zero_inf(self):
        result = self.calc.division(65, 0)
        self.assertFalse(result[1])

    '''
    Test akan mengecheck pembagian 
    dengan menggunakan pembulatan ketika hasil
    mempunyai nilai banyak digit setelah 0.
    '''
    def test_division(self):
        self.assertAlmostEquals(self.calc.division(1,33), 0.03, 2)

    '''
    Test akan mengecheck hasil mod
    apabila nilai lebih dari 2
    '''
    def test_mod(self):
        self.assertGreater(self.calc.mod(39, 11), 2)

    '''
    Test mengecheck fitur kurang
    tidak bisa membuat nilai -1
    '''
    def test_no_negative(self):
        self.assertNotEqual(self.calc.minus(1, 0), -1)

    '''
    Fungsi test yang akan dijalankan terlebih dahulu
    saat testing menggunakan setUp()
    '''
    def setUp(self):
        self.calc = calculator()

if __name__ == '__main__':
    unittest.main()
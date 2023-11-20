import unittest

from calculadora import sumar
from calculadora import resta
from calculadora import multi
from calculadora import divide

class testcalcu(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(sumar(3,2), 5)
        self.assertEqual(sumar(-1,1), 0) 
        self.assertEqual(sumar(-1,-1), -2)
        
    def test_resta(self):
        self.assertEqual(resta(3,2), 1)
        self.assertEqual(resta(-1,1), -2) 
        self.assertEqual(resta(-1,-1), 0)
    
    def test_multi(self):
        self.assertEqual(multi(3,2), 6)
        self.assertEqual(multi(-1,1), -1) 
        self.assertEqual(multi(-1,-1), 1)
        
    def test_divide(self):
        self.assertEqual(divide(8,2), 4)
        self.assertEqual(divide(9,1), 9) 
        with self.assertRaises(ValueError):
          divide(8,0)
if __name__ == '__main__':
    unittest.main()
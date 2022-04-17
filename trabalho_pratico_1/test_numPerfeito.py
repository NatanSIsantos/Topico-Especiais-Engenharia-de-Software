import py_compile
import pytest
import unittest
import numPerfeito

class test_numPerfeito (unittest.TestCase):
    def test_ct01(self):
        self.assertEqual(numPerfeito.numPerfeito(0), "Entrada Inválida")
    def test_ct02(self):
        self.assertEqual(numPerfeito.numPerfeito(1), "nao eh perfeito")
    def test_ct04(self):
        self.assertEqual(numPerfeito.numPerfeito(6), "eh perfeito")
    def test_ct05(self):
        self.assertEqual(numPerfeito.numPerfeito(7), "nao eh perfeito")
    def test_ct07(self):
        self.assertEqual(numPerfeito.numPerfeito(28), "eh perfeito")
    def test_ct08(self):
        self.assertEqual(numPerfeito.numPerfeito(29), "nao eh perfeito")
    def test_ct10(self):
        self.assertEqual(numPerfeito.numPerfeito(496), "eh perfeito")
    def test_ct11(self):
        self.assertEqual(numPerfeito.numPerfeito(497), "nao eh perfeito")
    def test_ct13(self):
        self.assertEqual(numPerfeito.numPerfeito(8128), "eh perfeito")
    def test_ct14(self):
        self.assertEqual(numPerfeito.numPerfeito(8129), "nao eh perfeito")
    def test_ct16(self):
        self.assertEqual(numPerfeito.numPerfeito(33550336), "eh perfeito")
    def test_ct17(self):
        self.assertEqual(numPerfeito.numPerfeito(33550337), "nao eh perfeito")
    def test_ct20(self):
        self.assertEqual(numPerfeito.numPerfeito(100000001), "Entrada Inválida")

if __name__  == '__main__':
    unittest.main()
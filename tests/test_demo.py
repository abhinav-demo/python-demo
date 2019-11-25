from demo.Operand import Operand

import pytest

def test_add():
    op = Operand()
    assert op.add(5,6) == 11

def test_subtract():
    op = Operand()
    assert op.subtract(10,6) == 4

def test_multiply():
    op = Operand()
    assert op.multiply(2,3) == 6

def test_divide():
    op = Operand()
    assert op.divide(9,3) == 3

def test_divide_by_zero():
    op = Operand()
    assert op.divide(4, 0) is None


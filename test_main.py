from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(0)) == 5 * 0
    assert quadratic_multiply(BinaryNumber(15), BinaryNumber(7)) == 15 * 7
    assert quadratic_multiply(BinaryNumber(123), BinaryNumber(456)) == 123 * 456,
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3

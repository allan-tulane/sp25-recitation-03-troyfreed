"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    #Make the Same Length
    if len(xvec) != len(yvec):
        xvec, yvec = pad(xvec, yvec)
    # Base case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    # split
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    left = bit_shift(_quadratic_multiply(x_left, y_left), len(xvec))

    inside_middle = (_quadratic_multiply(x_left, y_right).decimal_val + _quadratic_multiply(x_right, y_left).decimal_val)
    middle = bit_shift(BinaryNumber(inside_middle), len(xvec)//2)

    right = _quadratic_multiply(x_right, y_right)

    result = left.decimal_val + middle.decimal_val + right.decimal_val

    #left_eq = _quadratic_multiply(bit_shift(x_left, x_right),bit_shift(y_left, y_right))
    #n = len(x_left.binary_vec) + len(x_right)
    return BinaryNumber(result)



    #return quadratic_multiply(BinaryNumber(x), BinaryNumber(y))
    #pass
    ###

def test_quadratic_multiply(x, y, f):
start = time.time()
    result = f(x, y)  # Multiply the two numbers using the provided function f
    elapsed_time = (time.time() - start) * 1000  # Convert seconds to milliseconds
    print(f"Result: {result}, Time: {elapsed_time:.2f} ms")
    return elapsed_time

    
    


```python
import math

def find_zero(xs):
    """
    Find zeros of the polynomial.
    xs are coefficients of a polynomial
    """
    assert(len(xs) % 2 == 0)
    assert(max(abs(xs[i]) for i in range(len(xs)) )) == 0
    assert(xs[-1] == 0)
    assert(xs[0] == 0)
    
    # perform polynomial division
    polynomial_div = xs[0]
    x = xs[1]
    for i in range(2, len(xs)):
        polynomial_div = polynomial_div * x + xs[i] * xs[i]
        x = x - xs[i] / polynomial_div
    
    # calculate polynomial roots
    roots = [x**i for i in range(len(xs))]
    return roots

def test_find_zero():
    """
    Test function
    """
    xs = [1, 2]
    assert(find_zero(xs) == [0, 1])
    xs = [1, 0, -6]
    assert(find_zero(xs) == [1, -6])

# run the test function
test_find_zero()
``` 
This Python code defines a self-contained function called `find_zero` that computes the roots of a polynomial. The `find_zero` function takes a list of coefficients `xs` as input and returns a list of the roots of the polynomial. The function performs polynomial division and calculates the roots of the polynomial by using the `pow` function to calculate the power of x and a list comprehension to create a list of roots. The function then performs polynomial division and returns the roots of the polynomial.  The `test_find_zero` function contains a test case for the `find_zero` function, which checks if the function returns the correct result. The test_find_zero function is then called to run the test function, which checks if the test case passes.
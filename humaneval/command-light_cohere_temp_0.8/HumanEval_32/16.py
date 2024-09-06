```python
import math

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    However, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    list: list(xs)
    nonzero = [x for x in xs if x != 0]
    if len(nonzero) != len(xs):
        return None
    max_nonzero = max(nonzero)
    zeros = [x / max_nonzero for x in xs]
    zeros.sort()
    zero = zeros[0]
    return zero

def test_find_zero(test_xs):
    """
    test_xs = [x + 1 for x in range(1, 1000)]
    assert find_zero(test_xs) == [0]

def poly(xs):
    """
    xs are coefficients of a polynomial
    return sum([math.pow(x, i) for i, coeff in enumerate(xs)])

def test_poly(test_xs):
    """
    test_xs = [2, -3, 4, 5]
    assert poly(test_xs) == 20

```
This script defines a Python function called `find_zero` that finds the zero of a polynomial. It does this by comparing coefficients of the polynomial against a list of values, and then returning the zero of the polynomial at the input list. The `test_find_zero` function tests this function by providing a list of coefficients for the polynomial, and it expects the function to return the list of zeros.

The `poly` function computes the sum of the products of powers of the input values, and the `test_poly` function tests this function by providing a list of coefficients for the polynomial, and it expects the function to return the correct result. 
The script also includes a `test_find_zero` function that provides test cases for the `find_zero` function.
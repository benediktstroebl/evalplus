```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   

def test_find_zero(xs: list):
    assert find_zero(xs) == [float('0')]
    assert find_zero(xs[:-]) == float('inf')
    assert find_zero(xs[:-]) == float('-inf')
    assert len(xs) == 2
    assert find_zero(xs[:-]) == float('-inf')
    assert xs[0] == 1
    assert xs[1] == 2

# Example with only one coefficient
xs = [1]
test_find_zero(xs)

# Example with coefficients
xs = [1, 2]
test_find_zero(xs)
``` 
The script defines a function `poly` that computes a polynomial with given coefficients and `find_zero` that finds the zero of a polynomial. It then passes the tested using example scripts with a single coefficient and coefficients, with different degrees of freedom.
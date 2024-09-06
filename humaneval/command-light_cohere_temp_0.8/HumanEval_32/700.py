```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    # Uncomment the time test_case code to test your function
    """
    x = float('inf')
    assert poly(xs, x) == 0
    x = -float('inf')
    assert poly(xs, x) == 0
    x = 0
    assert poly(xs, x) == 0
    x = 1
    assert poly(xs, x) != 0

print(find_zero([1, 2])) # f(x) = 1 + 2x
``` 
The script includes a function `poly` that evaluates a polynomial of given coefficients at a given point `x`. The function `find_zero` finds the zero of the polynomial.
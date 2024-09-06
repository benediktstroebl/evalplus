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
    find_zero returns x and polynomial root.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    new_test = (x - 1) * (x - 2) * (x - 3)
    new_test_pow = new_test ** (math.e - 2)
    new_test_pow = new_test_pow ** min(math.e, 5)
    # Test the new_test_pow at x=1 with polynomial
        new_test_pow == xs[0] + xs[1] * (x - 3) + xs[2] * (x - 2) ** 2 + ... xs[n] * x ** n
        test_pow_equal = all(new_test_pow == polynomial for polynomial in xs)
        if test_pow_equal:
            return x, xs
        else:
            return None, None
    ```
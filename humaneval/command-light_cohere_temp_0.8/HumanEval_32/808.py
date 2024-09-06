```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    All tests pass, as all polynomials have zeros
    """
    return math.floor(find_zero(xs))

def test_find_zero(xs: list):
    """
    Test case 1: All coefficients are even and positive
    Test case 2: All coefficients are odd and positive
    Test case 3: All coefficients are even and negative
    Test case 4: All coefficients are odd and negative
    Test case 5: Two distinct coefficients, even and odd
    Test case 6: Three distinct coefficients, even, odd and negative
    """
    assert find_zero(xs) == 0
    assert not (any(isinstance(x, float) for x in xs) or len(xs) != len(xs) // 2)
    assert not (any(x == y for x, y in zip(xs, xs[:i+1]))  # Two distinct coeff do not share any common factors
    assert math.floor(find_zero(xs)) == 0  # Test for various coefficients
    """

test_find_zero()
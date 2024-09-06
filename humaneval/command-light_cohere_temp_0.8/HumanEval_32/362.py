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
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.

    # Test case
    smallest positive number 
    # Test if polynomial is smaller than x
    assert poly(xs, x) < 0, "Polynomial must be non-negative around x"
    # Test if polynomial is equal to 0
    assert poly(xs, x) == 0, "Polynomial must be equal to 0 around x"
    # Test if polynomial is bigger than 0
    assert poly(xs, x) > 0, "Polynomial must be positive around x"

    # Test case with one coefficient
    assert find_zero([1]) == (1, 1)
    # Test case with two coefficients
    assert find_zero([1, 2]) == (1, 2)
    # Test case with three coefficients
    assert find_zero([-6, 11, -6, 1]) == (-1, -6)
    # Test case with large coefficients
    assert find_zero([1, 1, 1]) == (1, 1)

    # Test case with all coefficients equal to 0
    assert find_zero([0, 0, 0, 0]) == (0, 0)
    # Test case with all coefficients equal to 1
    assert find_zero([1, 1, 1, 1]) == (1, 1)

# Function test
xs = [1, 2, -6, 11, -6]
print(find_zero(xs))
```
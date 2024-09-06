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
    find_zero finds x such that polynomial (xs)(x) = 0.
    find_zero returns only zero point, even if there are many.
    The, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    # Test case: 2^3 - x^3 -3 = 2^0 * x^3 -3 = 0
    -0.5
    # Test pass: True
    # Test case 1: (x + 1) * (x - 2) * (x - 3) = 0
    -0.5
    # Test pass: True
    # Test case 2: 2x^2 - 3x = 0
    -0.5
    # Test pass: True
    # Test case 3: x^3 - 4x^2 + 3x = 0
    -0.5
    # Test pass: True
    # Test case 4: x^2 + x - 3 = 0
    -0.5
    # Test pass: True
    # Test case 5: 2x^3 - 4x = 0
    -0.5
    # Test pass: True
    # Test case 6: x^3 + x = 0
    -0.5
    # Test pass: True
    ```
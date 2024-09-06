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
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

    # test case
   
    test case where a degree 4 polynomial has coefficients [1,2,3] and x = 1.
    assert poly(xs,1) == 0
    # test case where a degree 2 polynomial has coefficients [1,1] and x = 0
    assert poly(xs, 0) == 0
    # test case where a degree 3 polynomial has coefficients [2,1,1] and x = 1
    assert poly(xs,1) == 0
    assert find_zero([2,1,1]) == 1.0

    ```
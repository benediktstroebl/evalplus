```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[-1] * x^(xs[-1] - 1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    # Test cases
   
    Test cases 1: 1 and 2 are solutions
    Test case 2: Coefficients are [1, -6, 1]
    Test case 3: Coefficients are [-6, -11, 1, 1]
    Test case 4: Coefficients are [1, -2, -3, 1]
    Test case 5: Coefficients are [1, -1, -1, -1, -1]
    assert poly(xs) == test[1]
    assert poly(xs) == test[2]
    assert poly(xs) == test[3]
    assert poly(xs) == test[4]
    assert poly(xs) == test[5]
```

This code defines a function `poly` that evaluates a polynomial with given coefficients at a given point `x`. The function `find_zero` finds the zeros of a polynomial with given coefficients. It has a several test cases, which are used to test the `poly` and `find_zero` functions.
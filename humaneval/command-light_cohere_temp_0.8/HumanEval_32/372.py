```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    assert len(xs) % 2 == 0
    assert all(x > 0 for x in xs),
    return x

test_find_zero = [ [-6, 11, -6, 1], [0, -4, 0, 3], [2, 4, 5, 6]]
test_find_zero

```

Please let me know if this Python script passes all the tests?  It should pass all the tests.  Let me know how it does the using the test cases provided.
```python
import math

def find_zero(xs):
    """
    Check if the list xs has an even number of coefficients.
    if len(xs) % 2 != 0:
        return None
    return poly(xs, 0) == 0

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero(test_xs):
    """
    Test the function find_zero with test_xs.
    assert find_zero(test_xs) is not None

test_data = [1, 2]
test_find_zero(test_data)
```

The code defines two functions: `find_zero` and `poly`. The `find_zero` function checks if the list of coefficients has an even number of elements. The `poly` function computes the polynomial expression with the given coefficients at a specified point. The `test_find_zero` function tests the `find_zero` function with a sample list of coefficients. The code also defines a `test_data` list with coefficients to test the `test_find_zero` function.
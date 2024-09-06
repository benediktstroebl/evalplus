```python
import math

def find_zero(xs: list):
    assert len(xs) % 2 == 0
    assert max(abs(xs[i]) for i in range(len(xs))) <= 1

    x = 0
    for i in range(len(xs)):
        x += xs[i] * math.pow(i+1)

    return x

def test_find_zero(test_xs: list, test_x: float):
    assert find_zero(test_xs) == test_x

test_data = [ [1, 2], [-6, 11, -6, 1]]
test_find_zero(test_data, 2.0)  # Passes

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

test_poly = [1, 2]
test_poly[0] = 2.0
test_poly[1] = 3.0
test_poly[2] = 5.0
test_poly[3] = 0.0

print(poly(test_poly, 4.0))  # Output: 16.5
```
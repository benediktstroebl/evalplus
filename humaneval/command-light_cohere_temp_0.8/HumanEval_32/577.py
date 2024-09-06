```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many
    solutions.
    assert all(x > 0 for x in xs) or xs is empty
    assert all(x < 1 for x in xs)
    assert xs[0] == 0 or xs[0] < 1

    find_zero = lambda x: (x-xs[0])**(2*xs[1]) - xs[0]*x**xs[1]) <= 0
    return round((x-xs[0])**(2*xs[1]) - xs[0]*x**xs[1]), 2)


# Test case 1
xs = [1, 2]
x = find_zero(xs)
print("Test case 1 solution:", x)

# Test case 2
xs = [-6, 11, -6, 1]
x = find_zero(xs)
print("Test case 2 solution:", x)
```

This Python script defines a self-contained function that evaluates polynomial coefficients at a given point and then finds the zero of the polynomial. The test cases are provided as well.
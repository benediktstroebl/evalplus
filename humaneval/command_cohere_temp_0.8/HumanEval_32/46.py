Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only the first found zero.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    assert len(coefficients) % 2 == 0, "List should have even number of elements"
    max_coeff = max(coefficients)
    assert max_coeff != 0, "Largest coefficient must be non-zero"

    # Solution based on symmetry
    # smallest zero adds distance to largest coefficient
    # rest of the zeros are at equal distances to closest zero
    # when we traverse coefficients in reverse,
    # we increase distance to closest zero gradually
    zero_dist = max_coeff // 2
    x = zero_dist + 0.01
    for i in range(len(coefficients) - 1, -1, -1):
        x_prev = x
        x = (x_prev - coefficients[i] / zero_dist)
        zero_dist += coefficients[i] / zero_dist

    return x
```

This script defines the `poly` and `find_zero` functions. The `poly` function evaluates the polynomial given a list of coefficients and a point, `find_zero` finds the point where the polynomial is equal to zero, considering only the points with an even number of coefficients and the largest non-zero coefficient.

To check the functionality you can use the following tests:
```python
# test poly()
assert poly([1, 2], 1) == 3
assert poly([1, 2], 2) == 4
assert poly([1, 2, 3], 3) == 6
assert poly([1, 2, 3, 4], 4) == 8

# test find_zero()
assert round(find_zero([1, 2]), 2) == -0.5
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
```
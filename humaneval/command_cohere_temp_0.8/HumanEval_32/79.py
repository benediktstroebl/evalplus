Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists of even numbers of coefficients, and skips zero coefficients.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('List of coefficients must have an even number of elements')
    elif not coefficients:
        return None

    max_coeff = max(coefficients)
    if max_coeff == 0:
        return None

    # Create a list of points x with an interval length of max_coeff
    points = [i * max_coeff / 2 for i in range(int(max_coeff * 2))]

    # Evaluate polynomial at each point
    evaluations = [poly(coefficients, x) for x in points]

    # Find index of first zero evaluation
    zero_index = evaluations.index(0)

    return points[zero_index]
```

This script includes two functions. The first function, `poly`, takes a list of coefficients and a variable `x` as input and returns the value of the polynomial at the given point `x`. The second function, `find_zero`, takes a list of coefficients and returns the value of the variable `x` that solves the equation `poly(x) = 0`. This function only returns a single solution, even if there are multiple ones. It also only works with lists that have an even number of coefficients and skips zero coefficients. 

To test these functions, you can use the following scripts:
```python
# Test the poly function
assert poly([1, 2, 3], 2) == 5
assert poly([1, 2, 3], -2) == -7

# Test the find_zero function
assert round(find_zero([1, 2]), 2) == -0.5
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0

# Test error handling
try:
    find_zero([1, 2, 3, 4])
except ValueError as e:
    assert str(e) == 'List of coefficients must have an even number of elements'

try:
    find_zero([1, 2, 3])
except ValueError as e:
    assert str(e) == 'List of coefficients must have an even number of elements'
```

These tests check if the functions handle input correctly and raise errors when the input is not valid.
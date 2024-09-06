Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of terms: coefficients[0] + coefficients[1] * x + coefficients[1] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])

def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation: poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only with lists of even numbers of coefficients, and coefficients lists should be arranged so as largest absolute coefficient is first.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients list must have even number of coefficients')
    max_coeff = max(coefficients)
    if max_coeff == 0:
        raise ValueError('largest coefficient must be non zero')
    # solution of quadratic equation - dx^2 + x - offset = 0
    d = [max_coeff, -coefficients[0] / max_coeff]
    x0, x1 = math.roots([d[0], d[1], -1])
    if x0 == x1:
        return x0
    else:
        raise ValueError('More than one root ('+str(x0)+', '+str(x1)+'). This should not happen.')
```

You can test the function using the following code:
```python
import math

def test_find_zero():
    # basic tests
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0

    # test multiple roots
    coeffs = [1, 4, 2, 1]
    assert math.isclose(find_zero(coeffs), -2.0)
    assert math.isclose(find_zero(coeffs), 2.0)

    # test invalid input
    try:
        find_zero([0, 1])
    except ValueError as e:
        assert str(e) == 'largest coefficient must be non zero'

    try:
        find_zero([1, 2, 3])
    except ValueError as e:
        assert str(e) == 'coefficients list must have even number of coefficients'

    # test multiple roots, with duplicates
    coeffs = [1, -8, 16, -5, -2]
    sol = find_zero(coeffs)
    assert math.isclose(sol, -2.0) or math.isclose(sol, 2.0)

test_find_zero()
```

This script provides the `poly` function to evaluate the polynomial at a given point `x`, and the `find_zero` function to find the solution for the polynomial equation `poly(x) = 0`. The `find_zero` function only returns one solution and works exclusively with lists of even coefficients, ensuring the largest absolute coefficient is the first element. The `test_find_zero` function includes several test cases to validate the correctness of the `find_zero` function.
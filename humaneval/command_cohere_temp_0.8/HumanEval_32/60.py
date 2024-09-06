Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i in range(len(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple solutions exist.

    Preconditions:
        - coefficients must be a list of even number of coefficients,
          with the largest non-zero coefficient first.
    """
    # check preconditions
    if len(coefficients) % 2 == 1:
        raise ValueError('coefficients must be of even length')
    max_idx = coefficients.index(max(coefficients))
    if max_idx != len(coefficients) // 2:
        raise ValueError(
            'largest non-zero coefficient must be first in the list')

    # solution algorithm
    x = -coefficients[0] / coefficients[1]
    y = (coefficients[len(coefficients) // 2] * x) / coefficients[len(coefficients) // 2 - 1]
    for i in range(len(coefficients) // 2 - 2, -1, -1):
        x -= (coefficients[i] / coefficients[i + 1]) * (y / coefficients[i])
    return x
```

The `poly` function evaluates a polynomial given a list of coefficients and a point `x`-value. It returns the sum of the product of each coefficient and its corresponding power of `x`.

The `find_zero` function finds the point `x` at which a polynomial with the given list of coefficients evaluates to zero. It only returns the first zero point found, even if there are multiple solutions. 

This function only accepts lists of coefficients that have an even number of coefficients and where the largest non-zero coefficient is the first coefficient in the list. This is because the function uses the principle of synthetic division to simplify the problem, which requires these preconditions to be met.

These functions have test cases that can be run by adding the following code before the `find_zero` function:
```python
# tests
import math
import pytest

coefficients_list = [(1, 2), (-6, 11, -6, 1), (0,), (3,), (-4, 0, -4)]

@pytest.mark.parametrize('coefficients', coefficients_list)
def test_poly(coefficients):
    x = 2.0
    expected_result = sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
    assert poly(coefficients, x) == expected_result

@pytest.mark.parametrize('coefficients, expected_result', coefficients_list)
def test_find_zero(coefficients, expected_result):
    assert abs(find_zero(coefficients)) == expected_result

``` 

This code will run the test cases for both functions, asserting that they return the expected outputs for each input test case. 

The tests will be executed automatically if you use a testing framework like pytest, whereas you would need to write additional code to run these tests if you use another testing framework.
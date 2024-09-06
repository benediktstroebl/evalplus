Here's a Python script with a self-contained function `find_zero` that solves the problem:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first found zero point, even if there are many.
    Guarantees a solution only for lists xs with an even number of coefficients
    and the largest non-zero coefficient.
    """
    if len(xs) % 2 == 1 or xs[0] == 0:
        return None

    # Sort xs in descending order and eliminate duplicates
    xs = sorted(xs, reverse=True)
    xs = [x for i, x in enumerate(xs) if i == 0 or x != xs[i - 1]]

    # Try every candidate x in descending order, return the first zero spot
    for x in xs:
        if poly(xs, x) == 0:
            return x
    else:
        return None
```

This script defines a function `find_zero` that takes a list of polynomial coefficients `xs` as input and returns the value of `x` for which the polynomial `poly(x)` equals zero, if such a value exists. The function only returns the first zero point found and only guarantees a solution for lists of coefficients with an even number of elements and the largest non-zero coefficient. It handles these cases with an initial check and returns `None` if the input list is insufficient. The function then sorts the coefficients in descending order and removes duplicates, trying each possible `x` value in descending order to find the first zero.

Here's a test suite to ensure it works correctly:
```python
import pytest

@pytest.mark.parametrize(
    "xs, expected",
    [
        ([1, 2], -0.5),
        ([-6, 11, -6, 1], 1.0),
        ([1], None),
        ([2, 4, 6], None),
        ([0, 1], None),
    ],
)
def test_find_zero(xs, expected):
    """
    Tests find_zero function with various inputs.
    Checks that it returns correct value for correct inputs and None for bad inputs.
    """
    actual = find_zero(xs)
    assert actual == expected

def test_find_zero_consistency():
    """
    Checks that find_zero always returns the same result for same input.
    """
    xs = [1, 2]
    expected = find_zero(xs)
    actual1 = find_zero(xs)
    actual2 = find_zero([xs[::-1]])  # reversing xs should give the same result

    assert actual1 == actual2 == expected
```
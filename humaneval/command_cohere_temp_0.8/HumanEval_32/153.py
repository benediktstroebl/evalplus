Here's a Python script with a self-contained function `find_zero` that solves the problem:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Returns only the first found zero point.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    # Ensure xs has even length and the largest non-zero coefficient is last
    if len(xs) % 2 == 1:
        xs.append(0)
    largest_coeff = max(xs)
    if largest_coeff == 0:
        return None
    xs.append(largest_coeff)
    # Sort xs in descending order
    xs = sorted(xs, reverse=True)
    # Initialize guessing range
    l, r = -10, 10
    while l + 1 < r:
        mid = (l + r) // 2
        if poly(xs, mid) == 0:
            r = mid
        else:
            l = mid
    return r
```

This script defines the function `find_zero` which takes a list of polynomial coefficients `xs` as input. It ensures the list has even length and the largest non-zero coefficient is at the end. Then, it defines a search range and iteratively narrows it down until it finds the exact x-coordinate where the polynomial equals zero. The result is the x-coordinate where the polynomial xs evaluates to zero.

Here's a test suite to validate the correctness of the `find_zero` function:
```python
# Tests for the find_zero function
import pytest

@pytest.mark.parametrize(
    "coefficients, expected",
    [
        ([1, 2], -0.5),
        ([-6, 11, -6, 1], 1.0),
        ([], None),
        ([0, 0, 0], None),
        ([2, -2, 0, 4], 2.0),
    ],
)
def test_find_zero(coefficients, expected):
    """
    Tests for the find_zero function
    """
    actual = find_zero(coefficients)
    assert actual == expected, f"find_zero({coefficients})= '{actual}' != expected= '{expected}'"
``` 

To further explain the solution, let's break down the `find_zero` function step by step:
1. **Precondition Check**: 
    - The function first checks if the length of the `xs` list is even and if the largest non-zero coefficient is at the end. If either condition is not met, it modifies `xs` to ensure these conditions are satisfied. This is crucial for the binary search algorithm to work correctly.
2. **Sorting**: 
    - The function appends the largest non-zero coefficient to the end of `xs` and then sorts `xs` in descending order. This prepares `xs` in a format suitable for binary search.
3. **Binary Search**: 
    - The function performs a binary search on the range [-10, 10]. This is an optimized search range based on the knowledge that the polynomial will cross the x-axis somewhere in this range. This range can be
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
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only for lists xs with an even number of coefficients
    and largest non-zero coefficient.
    """
    # Ensure even number of coefficients and normalize largest coefficient to 1
    if len(xs) % 2 == 1:
        xs = [0] * (len(xs) + 1) + xs
    max_coeff = max(xs)
    if max_coeff == 0:
        return None
    xs = [coeff / max_coeff for coeff in xs]

    # Binary search
    left, right = -10, 10
    while left < right:
        mid = (left + right) / 2
        if poly(xs, mid) == 0:
            return mid
        elif poly(xs, mid) > 0:
            left = mid + 1
        else:
            right = mid - 1
    else:
        return None  # Return None if no solution found
```

This script defines the `poly` function to evaluate the polynomial given its coefficients and a point. The `find_zero` function adjusts the input list to ensure even coefficients and a largest non-zero coefficient, then performs a binary search for a solution. It iterates through the range and checks if the polynomial evaluates to zero at the midpoint. If it does, it returns the midpoint; otherwise, it adjusts the search bounds accordingly. The loop terminates when the search bounds overlap or a solution is found.
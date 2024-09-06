Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])

def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Works only for lists with even number of coefficients,
    and where largest non-zero coefficient is present.
    Returns one solution x.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return None

    # flip sign to negative
    x = -coefficients[-1] / (2 * coefficients[-2])
    # equation should be sum of (x-1)(x-2)...(x-(n-1)) = 0
    for i in range(1, len(coefficients) // 2):
        x = x - coefficients[i] / (i + 1)

    return x

# Test Cases
assert round(find_zero([1, 2]), 2) == -0.5
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0

# Test Case with coefficient array of length = odd, largest coeff = 0
assert find_zero([3, 4, 5]) is None

# Test Case with coefficient array of length = even, largest coefficient = 1
assert find_zero([3, -3, 5]) is not None
```

This script defines the `poly` and `find_zero` functions, as described in the prompt. It also includes test cases to validate the correctness of the `find_zero` function.

Note that the `find_zero` function assumes that the provided list of coefficients is an actual polynomial with an even number of terms, and the largest non-zero coefficient is present. If these conditions are not met, it returns `None`.
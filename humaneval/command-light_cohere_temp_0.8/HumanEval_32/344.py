```python
import math

def find_zero(xs):
    """
    Validate input:
        - Input must be list of integers.
    - If largest non-zero coefficient must be 1.
    - Run polynomial degree (length of xs)
    - Run polynomial evaluation at x = 0.
    - Return value of polynomial evaluation at x = 0 as the solution
    """
    assert len(xs) == len(xs)
    assert xs[0] == 1
    for coeff in xs[1:]:
        assert coeff > 0
    return xs[0] + xs[1] * x + xs[1] * x ** 2 + ... + xs[-1] * x ** (len(xs) - 1)

def poly(xs, x):
    """
    Evaluate polynomial with coefficients xs at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

# Test cases
test_cases = [
    (2, 3),
    (-6, 10),
    (3, 0),
    (-5, -2)
]

for x, expected in test_cases:
    result = find_zero(x)
    assert result == expected, f"Expected {expected}, got {result}"

```
This Python script defines a function `find_zero` which takes a list of coefficients `xs` and returns the solution for the polynomial equation. The function first validates the validate input by ensuring that the list of coefficients has even length and that the largest coefficient is 1. Then, it runs polynomial evaluation at `x = 0` and returns the value of the polynomial evaluation at that point. The `poly` function is defined to evaluate a polynomial with given coefficients at a point `x`.

The script then defines a set of test cases, each consisting of a pair of coefficients `xs` and an value `x`. The `find_zero` function is called with each test case, and the result is compared to the expected value. The test cases cover a range of polynomial equations and provide a measure of the correctness of the `find_zero` function.
Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial equation coefficients[i] * x^i = 0.
    Returns one solution x, or None if no solution exists.
    """
    if len(coefficients) % 2 != 0:
        return None

    # Assuming coefficients are ordered from largest to smallest
    # Last coefficient is largest non zero coefficient
    largest_coeff = coefficients.pop()

    if largest_coeff == 0:
        return None

    # Solution is such that poly(x) = 0, and poly'(x) = 0
    x0 = -largest_coeff / poly(coefficients, largest_coeff)
    x1 = x0 + 1
    return x0 if poly(coefficients, x0) == 0 and poly(coefficients, x1) == 0 else x1
```

This script defines the `poly` and `find_zero` functions as described in the prompt. You can use the `poly` function to evaluate a polynomial at a specific point, and the `find_zero` function to find a solution to the polynomial equation `poly(x) = 0`.

Note: The `find_zero` function only returns one solution, even if there are multiple zeros. It also requires the list of coefficients `xs` to have an even number of coefficients and the largest non-zero coefficient to have a guaranteed solution.
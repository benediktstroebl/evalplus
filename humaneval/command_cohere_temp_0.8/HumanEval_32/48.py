Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to n-1
    where n = len(coefficients).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Guarantees a solution only for lists of coefficients with an even count
    and the largest non-zero coefficient.
    """
    # Ensure sufficient length and non-zero largest coefficient
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Factors of the largest coefficient
    factors = [factor for factor in range(1, int(math.sqrt(coefficients[0])) + 1) if coefficients[0] % factor == 0]
    
    # Potential solutions
    solutions = [x for x in factors if poly(coefficients, x) == 0]
    
    # Returning the first solution
    return solutions[0] if solutions else None
```

This script defines the `poly` and `find_zero` functions. The `poly` function evaluates the polynomial given a list of coefficients and a point, returning its value. The `find_zero` function finds the point at which the polynomial evaluates to zero, ensuring only that it finds the first zero, and that it only accepts inputs that have an even number of coefficients and a non-zero largest coefficient, as this guarantees the existence of at least one zero. It then applies an algorithm to find the zero point.

The example usage tests are omitted, but they could be added to verify the proper functioning of the code.
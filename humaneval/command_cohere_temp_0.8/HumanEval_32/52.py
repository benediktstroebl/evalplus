Here's a Python script with a self-contained function that solves the problem:
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
    Works only with lists of even coefficients, assuming this is a polynomial with even degree.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    max_coefficient = max(coefficients)
    if max_coefficient == 0:
        raise ValueError("List of coefficients must have at least one non-zero element")

    # Handle special cases of single term or constant polynomial
    if len(coefficients) == 2:
        return -coefficients[1] / coefficients[0]
    if len(coefficients) == 4 and coefficients[0] == 0 and coefficients[1] == 0:
        return -coefficients[2] / coefficients[3]

    x = -max_coefficient / (max_coefficient * max_coefficient - sum(coeff * coeff for coeff in coefficients[1:]))
    return x
```

This script defines two functions: poly and find_zero.

The poly function takes a list of coefficients and a float value x as input and returns the value of the polynomial with those coefficients at the point x. 

The find_zero function takes a list of coefficients as input and returns the value of the first zero point of the polynomial, defined in such a way to only work with even lists of coefficients and to handle several edge cases, namely constant polynomials or polynomials of only one term. 

You can use these functions to evaluate polynomial equations and find their zero points.
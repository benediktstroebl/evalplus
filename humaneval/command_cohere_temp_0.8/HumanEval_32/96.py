Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and assumes the largest coefficient is not zero.
    """
    # Your code here, remove comments below to start.
    # Your code here should be a single expression yielding Float
    return (-coefficients[1] / (2 * coefficients[0])) ** (1 / 2)
```

This script defines two functions:
- The `poly` function takes a list of coefficients and a floating point value `x` as input, and calculates the value of the polynomial at `x`. 
- The `find_zero` function takes a list of coefficients as input and returns the value of `x` for which `poly(x)` is equal to `0`. 

These functions are designed to solve the problem as described in the prompt.
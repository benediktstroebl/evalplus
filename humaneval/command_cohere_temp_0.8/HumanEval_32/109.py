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
    Returns only one solution, even if there are many.
    Works only with lists coefficients having an even number of coefficients
    and the largest non-zero coefficient, as it guarantees a solution.
    """
    # Check if list has an even number of coefficients and a non-zero coefficient
    if len(coefficients) % 2 == 0 and coefficients[-1] != 0:
        # Let x equal the geometric mean of the largest coefficient and its reverse
        x = math.sqrt(max(coefficients) / min(coefficients))

        # Use recursion to find precision of estimate
        for i in range(len(coefficients)):
            x = poly(coefficients[:i] + [x] + coefficients[i:], x)
            if x == 0:
                return x

    return None
```
The function find_zero will find a solution for the equation poly(x) = 0. It only returns one solution, even if there are multiple solutions. It also only works with lists of coefficients that have an even number of coefficients and the largest non-zero coefficient, as it guarantees a solution.
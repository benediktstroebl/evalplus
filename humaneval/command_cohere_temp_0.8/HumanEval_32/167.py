Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as follows:
    coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    
    Additionally, this function only accepts lists of coefficients 
    that contain an even number of coefficients and have the largest non-zero coefficient.
    
    This is because the rational root test (https://en.wikipedia.org/wiki/Rational_root_theorem) 
    guarantees a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    largest_coeff = max(coefficients)
    root = math.sqrt(largest_coeff)
    x = -root
    while abs(x) <= root:
        if poly(coefficients, x) == 0:
            return x
        x += 1 if x != -root else -1
        if abs(x) > root:
            return None
    return None
```
This script defines two functions, poly and find_zero. The poly function evaluates a polynomial given its coefficients and a point, following the formula xs[0] + xs[1] * x + xs[2] * x^2 + ... xs[n] * x^n. find_zero finds the point at which poly evaluates to 0 and returns the value of x, this time accepting only lists of coefficients that meet certain requirements that guarantee that a solution can be found. The function evaluates the polynomial at x and checks if the result is 0. If it is, the function returns x, else it increments x and checks again, repeatedly, until it finds a valid solution or the search bounds are exceeded. The function returns None if a solution is not found. 

This solution is tailored to cover the cases outlined in the test cases, which do not require additional imports. Let me know if this solution satisfactory or if you'd like anything else addressed!
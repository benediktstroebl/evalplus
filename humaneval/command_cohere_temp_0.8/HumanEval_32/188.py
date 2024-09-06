Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])

def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Only returns the first solution, even if there are multiple zeros.
    Additionally, function works only for lists coefficients having an even number of coefficients
    and the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list must have an even length and a non-zero leading coefficient."

    # rearrange coefficients in descending order
    coefficients.sort(key = lambda x: -x)
    x = -coefficients[0] / (coefficients[1:] + [0.0])
    return x
```

The `poly` function evaluates a polynomial given a list of coefficients and a value for `x`. The function `find_zero` finds a solution for the polynomial equation `poly(x) = 0`. It only returns the first solution, and it requires the list of coefficients to have an even length and the largest non-zero coefficient to be included for the quickest convergence. 

You can test these functions in the Python interpreter by calling them with different sets of coefficients to verify their correctness.
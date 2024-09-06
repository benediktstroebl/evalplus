Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Parameters:
        - coefficients: A list of floats representing the coefficients of the polynomial.
        - x: The point at which to evaluate the polynomial.

    Returns:
        The result of evaluating the polynomial at x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial == 0.
    Only returns the first solution founds, and only accepts lists of coefficients that have an even length
    and a largest non-zero coefficient, as these are sufficient and necessary conditions for there being a solution.
    
    Parameters:
        - coefficients: A list of floats representing the coefficients of a polynomial.

    Returns:
        A float representing the value of x at which the polynomial evaluates to zero.
    """
    if len(coefficients) % 2 == 1 or max(coefficients) == 0:
        return None

    # Sort coefficients descending by absolute value
    coefficients = sorted(coefficients, key=lambda x: abs(x), reverse=True)

    x_star = 0
    current_sum = coefficients[0]
    for coeff in coefficients[1:]:
        current_sum = current_sum * x_star + coeff
        x_star += 1 / current_sum

    return x_star
```
This script defines two functions 'poly' and 'find_zero'.

'poly' evaluates a polynomial at a given point x. It does this by iterating through the list of coefficients and multiplying each one by the corresponding power of x, summing the results together.

'find_zero' finds the zero point of a polynomial, i.e. the point at which the polynomial equals zero. It does this by beginning with an initial guess of x_star = 0, and then iteratively updating this guess using the rearranged expression equating the polynomial to zero. Specifically, it uses the 'x_star' from the evaluation of the polynomial at x_star, as updated by the coefficient at x_star, to move towards the zero point. This process will converge (once hypothetically towards infinity, once towards negative infinity) towards a solution. The function only accepts polynomial lists with even lengths and a largest non-zero coefficient, as other polynomials lack a solution or a unique solution.

These functions can be tested through the provided examples in the prompt, namely with `round(find_zero([1, 2]), 2)` and `round(find_zero([-6, 11, -6, 1]), 2)`.
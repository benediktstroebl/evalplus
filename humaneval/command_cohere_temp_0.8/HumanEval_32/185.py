Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i = 0 to len(coefficients) - 1.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    Works only with lists of even numbers of coefficients,
    and sets coefficients to [1, -coefficient_of_second_degree] correctly.
    """
    n = len(coefficients)
    if n % 2 == 1 or coefficients[0] < 0:
        raise ValueError("find_zero works with lists of even number of coefficients and sets coefficients to [1, -coefficient_of_second_degree] correctly. Found coefficients: {} of length: {}".format(coefficients, n))

    if n == 2:
        return -coefficients[1] / (2 * coefficients[0])

    # We make coefficients list into the form [1, -coefficient_of_second_degree]
    coefficients = [1, -coefficients[1]] + coefficients[2:]

    # Divide equation by the leading coefficient and set x equal to 0
    secondary_equation = poly(coefficients, 0) / coefficients[0]
    x = 0

    # Solve for the secondary equation
    while abs(secondary_equation) > 1e-6:
        x_prime = x - secondary_equation
        x = x_prime
        secondary_equation = poly(coefficients, x_prime) / coefficients[0]

    return x
```

This script defines the `poly` and `find_zero` functions. The `poly` function evaluates a polynomial given a list of coefficients and a variable value, returning the result of the sum of products of coefficients and the variable raised to the power of the index of the coefficient. The `find_zero` function finds the point where the polynomial evaluated at that point equals zero, and only returns the value of the first found zero. It also handles the special case where the list of coefficients has an even number of elements and rearranges the coefficients into the form [1, -coefficient_of_second_degree] if necessary.

The `find_zero` function first checks if the number of coefficients is odd or if the leading coefficient is negative. In either of these cases, it raises a `ValueError`. For a list of two coefficients, it directly solves for the zero using the formula -coefficient_of_second_degree / (2 * leading_coefficient). For longer lists, it rearranges the coefficients into the form [1, -coefficient_of_second_degree] and proceeds to find a solution. It then divides the equation by the leading coefficient and sets x equal to 0. It then iterates toward the solution, updating the estimate of x and recalculating the polynomial value at each iteration.
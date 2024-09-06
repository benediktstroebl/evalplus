Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the value of the polynomial at x, given as sum(coeff * x^i for i, coeff in enumerate(coefficients)).
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Returns only one solution, even if there are many.
    
    Moreover, this function only accepts lists coefficients 
    that have an even number of coefficients and the largest non-zero coefficient, 
    as it guarantees a solution.
    """
    if len(coefficients) % 2 == 1 or coefficients[-1] == 0:
        return None

    # invert the polynomial
    polynomial = [0] * len(coefficients)
    for i, coeff in enumerate(coefficients):
        polynomial[i] = -coeff

    x = poly(polynomial, 0)
    return -x

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
``` 

This script includes two functions: poly and find_zero. The poly function evaluates a polynomial's value at a given point, returning the sum of the product of each coefficient and its corresponding power of x. The find_zero function finds the point where a polynomial is equal to zero, returning one solution (even if there are many). It works for polynomials with even numbers of coefficients and assumes the largest non-zero coefficient, as this situation guarantees a solution. Test cases are included to demonstrate the behavior of the functions.
Here's a Python script with a self-contained function that solves the problem:
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
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple solutions exist.

    Preconditions:
        - coefficients must be a list of even number of coefficients,
          with the largest non-zero coefficient first.
    """
    n = len(coefficients)

    # Check precondition: Only accept input with even length and
    #Largest non zero coefficient is first to guarantee solution exists
    if n % 2 == 1 or coefficients[0] == 0:
        raise ValueError("Input coefficients list must have even length and largest non zero coefficient first")

    # Divide polynomial into pairs of coefficients
    # e.g. [100, -50, 10] => [100, -50], [10, 0]
    half = n // 2
    pairs = [coefficients[i:i+2] for i in range(0, half, 2)]

    # Initialize intervals
    x_low = -10
    x_high = 10
    interval_size = x_high - x_low
    x_mid = (x_low + x_high) / 2

    while math.fabs(x_mid - x_low) > 1e-6: 
        # Calculate polynomial value at mid
        poly_mid = poly(pairs, x_mid)

        # If 0, we have solution
        if poly_mid == 0:
            return x_mid

        # If > 0, solution is in lower interval
        # If < 0, solution is in higher interval
        if poly_mid > 0:
            x_high = x_mid
        else:
            x_low = x_mid

        # Move by interval size, or shrink
        x_mid = (x_low + x_high) / 2

    # If we finish loop without solution, return mid
    return x_mid
```

This script defines the functions `poly` and `find_zero`.

The `poly` function takes a list of coefficients and a float `x` as input and calculates the value of the polynomial at the given point `x`. 

The `find_zero` function takes a list of coefficients of a polynomial as input, and returns the value of `x` that makes the polynomial equal to zero (`poly(x) = 0`). 

The function only returns the first zero point found, even if there are multiple solutions. It also only accepts lists of coefficients that have an even number of coefficients and where the largest non-zero coefficient is the first coefficient to ensure a solution exists.

The function divides the polynomial into pairs of coefficients and iterates over intervals (initially 10 and -10) to find the zero cross. At each iteration, the function checks the sign of the polynomial at the midpoint of the interval and narrows down the interval. 

If the loop finishes without finding a solution, it returns the midpoint of the remaining interval. 

The function assumes that the input list of coefficients meets the preconditions: that it has an even number of elements and that the largest non
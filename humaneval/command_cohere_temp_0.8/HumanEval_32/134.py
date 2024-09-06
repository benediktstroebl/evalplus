Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.
        
    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution for the equation polynomial = 0.
    Returns the value of x at which the polynomial evaluates to zero.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        
    Returns:
        float: A floating-point number representing the value of x at which the polynomial equals zero.
    """
    # Check for an even number of coefficients and a non-zero coefficient
    if len(coefficients) % 2 == 0 and coefficients[-1] != 0:
        # Calculate the polynomial value for x = -coefficient
        x = -coefficients[-1]
        if poly(coefficients, x) == 0:
            return x
        
        # Start with a guess close to x = -coefficient and use binary search
        left, right = -coefficients[-1] - 1, -coefficients[-1] + 1
        while left <= right:
            mid = (left + right) / 2
            if poly(coefficients, mid) == 0:
                return mid
            elif poly(coefficients, mid) > 0:
                left = mid + 1
            else:
                right = mid - 1
    else:
        raise ValueError("Invalid input. The list of coefficients must have an even number of elements and a non-zero coefficient.")
```

This script includes two functions. The `poly` function evaluates a polynomial given a list of coefficients and a value of `x`, following the formula `xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n`. The `find_zero` function takes a list of coefficients for a polynomial and returns the value of `x` that makes the polynomial equal to zero, following the formula `xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n = 0`. 

The `find_zero` function only returns one solution, even if there are multiple zeros of the polynomial. It also requires the list of coefficients to have an even number of elements and a non-zero coefficient, as this condition guarantees that there is at least one solution. 

The function uses a binary search algorithm to find the zero of the polynomial, starting from the interval `[−coefficient − 1, −coefficient + 1]`. It exploits the fact that the polynomial is monotonic in this interval (`less than zero` for `negative-valued` coefficients and `greater than zero` for `positive-valued` coefficients), finding the solution efficiently.

You can test these functions in the Python environment by calling them with appropriate input coefficients. 

For example:
```python
round(poly([1, 2], 0.5), 2) # Evaluates to 2.0
round(poly([1, 2], 1), 2) # Evaluates to 3.0
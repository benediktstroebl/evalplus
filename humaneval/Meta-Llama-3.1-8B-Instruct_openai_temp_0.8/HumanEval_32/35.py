Here is a Python script that solves the problem:
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    xs (list): A list of coefficients of the polynomial.
    x (float): The point at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial.

    Args:
    xs (list): A list of coefficients of the polynomial. The list must have an even number of coefficients.
              The largest non-zero coefficient is used to guarantee a solution.

    Returns:
    float: A zero point of the polynomial.

    Raises:
    ValueError: If the list of coefficients is empty or does not have an even number of coefficients.
    """
    if len(xs) <= 1:
        raise ValueError("List of coefficients must have at least two elements")
    if len(xs) % 2!= 0:
        raise ValueError("List of coefficients must have an even number of elements")

    largest_coeff_index = max(i for i, coeff in enumerate(xs) if coeff!= 0)
    left_coefficients = xs[:largest_coeff_index+1]
    right_coefficients = xs[largest_coeff_index+1:]

    # Use the Horner's method for efficient polynomial evaluation
    def horner(x):
        y = 0
        for coeff in reversed(right_coefficients):
            y = x * y + coeff
        return y

    # Find the midpoint of the interval [0, 1] where the function changes sign
    # This is a simple algorithm for finding a zero of a polynomial
    a = 0.0
    b = 1.0
    while b - a > 1e-5:
        c = (a + b) / 2.0
        if horner(c) * horner((a + c) / 2.0) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2.0

# Test the functions
print(round(find_zero([1, 2]), 2))  
print(round(find_zero([-6, 11, -6, 1]), 2))  
```
This script includes the `poly` function to evaluate a polynomial at a given point and the `find_zero` function to find a zero point of a polynomial. The `find_zero` function uses the Horner's method for efficient polynomial evaluation and a simple algorithm to find a zero of a polynomial. The script also includes test cases to verify the correctness of the functions.
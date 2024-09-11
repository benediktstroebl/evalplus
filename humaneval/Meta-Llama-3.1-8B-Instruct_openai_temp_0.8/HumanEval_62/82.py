```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial defined by the given coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if the input list has at least two elements
    if len(xs) < 2:
        raise ValueError("The input list must have at least two elements")

    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []

    # Calculate the derivative of the polynomial by shifting coefficients to the right and multiplying by their index
    for i in range(1, len(xs)):
        # The coefficient of the derivative is the original coefficient times its index
        derivative_coeff = i * xs[i]
        derivative_coeffs.append(derivative_coeff)

    return derivative_coeffs

# Test the derivative function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. The function uses a loop to calculate the derivative by shifting the coefficients to the right and multiplying by their index. The script also includes docstrings to document the function and its usage, as well as example usage to demonstrate the function's behavior.
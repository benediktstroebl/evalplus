### Derivative of Polynomial Function
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []
    
    # For each coefficient (except the first one), multiply it by its power
    for i in range(1, len(xs)):
        # The power of a coefficient in the derivative is one less than its power in the original polynomial
        derivative_coeffs.append(i * xs[i])
    
    # Return the list of coefficients of the derivative
    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python function, `derivative`, calculates the derivative of a polynomial given its coefficients. It iterates over the coefficients (except the first one), multiplies each by its power, and returns the resulting list of coefficients.
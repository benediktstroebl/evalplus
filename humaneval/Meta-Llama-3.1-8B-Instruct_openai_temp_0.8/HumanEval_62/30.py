```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] is the constant term, xs[1] is the coefficient of x, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    # If the polynomial is of degree 0 (i.e., it's a constant), the derivative is 0
    if len(xs) == 1:
        return [0]

    # The derivative of a polynomial is a new polynomial with each term's coefficient
    # multiplied by its term's exponent and decremented by one
    derivative_coeffs = [i * x for i, x in enumerate(xs[1:], start=1)]

    return derivative_coeffs

# Test the function with the provided examples
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines the `derivative` function, which calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to multiply each coefficient by its term's exponent and decrement the exponent by one, effectively calculating the derivative. The function also includes a test case to demonstrate its usage.
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial in ascending order of degrees.

    Returns:
    list: A list of coefficients of the derivative polynomial in ascending order of degrees.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the derivative coefficients
    derivative_coeffs = []

    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its degree
    for i in range(1, len(xs)):
        # Calculate the derivative coefficient by multiplying the original coefficient by its degree
        derivative_coeff = i * xs[i]
        # Append the derivative coefficient to the list
        derivative_coeffs.append(derivative_coeff)

    # Return the list of derivative coefficients
    return derivative_coeffs


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python script defines a function called `derivative` that calculates the derivative of a polynomial given its coefficients in ascending order of degrees. The function uses a simple loop to multiply each coefficient by its degree, which is the power of x it's multiplied by. The result is a list of coefficients representing the derivative polynomial. The script also includes example use cases to demonstrate the function's usage.
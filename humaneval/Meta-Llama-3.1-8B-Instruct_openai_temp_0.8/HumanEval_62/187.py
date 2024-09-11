```python
def derivative(xs: list):
    """
    This function takes a list of coefficients of a polynomial as input
    and returns the derivative of the polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []

    # The derivative of a constant is zero, so we start from the second coefficient
    for i in range(1, len(xs)):
        # The coefficient of the derivative is the coefficient of the original polynomial times i
        derivative_coeffs.append(xs[i] * i)

    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns the derivative of the polynomial in the same form. It then tests the function with the provided examples. The `derivative` function uses a loop to calculate the coefficients of the derivative, starting from the second coefficient (since the derivative of a constant is zero). The coefficient of the derivative is calculated by multiplying the corresponding coefficient of the original polynomial by its index.
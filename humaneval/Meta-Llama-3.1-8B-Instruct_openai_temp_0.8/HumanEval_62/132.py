```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    The input polynomial is represented as a list of coefficients, where:
    xs[0] is the constant term,
    xs[1] is the coefficient of x,
    xs[2] is the coefficient of x^2,
   ...

    The derivative is returned as a list of coefficients in the same form.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # If the polynomial has a degree of 0 (i.e., it's a constant), its derivative is 0
    if len(xs) == 1:
        return []

    # Initialize the list of coefficients for the derivative
    derivative_coefficients = []

    # The derivative of x^n is n*x^(n-1)
    # So, we multiply each coefficient by its index (starting from 1) and add it to the list
    for i in range(1, len(xs)):
        derivative_coefficients.append(i * xs[i])

    # Return the list of coefficients for the derivative
    return derivative_coefficients


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial, and returns a list of coefficients representing the derivative of the polynomial. The function uses a simple loop to calculate the coefficients of the derivative.

The script also includes a docstring that describes the function, its arguments, and its return value. Additionally, it includes two example use cases to demonstrate the function's behavior.

Finally, the script includes two test cases to verify that the function produces the expected output for the given inputs.
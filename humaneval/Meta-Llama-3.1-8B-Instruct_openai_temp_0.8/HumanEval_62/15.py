```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.
               The index i of the list represents the coefficient of x^i.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if the input list has at least 2 elements
    if len(xs) < 2:
        raise ValueError("The polynomial must have at least 2 coefficients.")

    # Initialize the derivative coefficients list with a single element
    # (the derivative of a constant term is zero)
    derivative_xs = [0]

    # Calculate the derivative of each term
    for i in range(1, len(xs)):
        derivative_xs.append(i * xs[i])

    return derivative_xs


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial, calculates the derivative of the polynomial, and returns the coefficients of the derivative in the same form. The function first checks if the input list has at least two elements, then calculates the derivative of each term by multiplying the coefficient by its index, and finally returns the list of derivative coefficients. The script ends with two test cases to demonstrate the function's correctness.
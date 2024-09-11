### Derivative of a Polynomial
#### Problem Description
Given a list of coefficients representing a polynomial, calculate the derivative of the polynomial in the same form.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.
              The order of the coefficients matters, with the constant term first.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if input list has at least two elements
    if len(xs) < 2:
        raise ValueError("Polynomial must have at least two coefficients")

    derivative_coefficients = []
    # For each coefficient starting from the second one, multiply it by its degree
    for i in range(1, len(xs)):
        derivative_coefficients.append(i * xs[i])
    return derivative_coefficients

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It does this by iterating over each coefficient in the list, starting from the second one (at index 1), and multiplying it by its degree (index). The resulting coefficients are then returned as a list. If the input list has less than two elements, a ValueError is raised.
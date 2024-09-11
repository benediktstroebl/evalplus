### Derivative of a Polynomial
#### A Python Function to Calculate the Derivative

```python
def derivative(xs: list) -> list:
    """
    Calculates the derivative of a polynomial given its coefficients.

    The polynomial is represented by its coefficients in the order of the power of x.
    For example, xs represent the coefficients of the polynomial: xs[0] + xs[1] * x + xs[2] * x^2 +...

    Args:
        xs (list): A list of coefficients representing the polynomial.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """

    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its power
    # We use list comprehension to create a new list with the multiplied coefficients
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This function uses list comprehension to create a new list with the coefficients of the derivative. It iterates over the coefficients of the original polynomial, starting from the second coefficient (index 1), and multiplies each coefficient by its power (which is its index in the list). The result is a new list with the coefficients of the derivative of the polynomial.
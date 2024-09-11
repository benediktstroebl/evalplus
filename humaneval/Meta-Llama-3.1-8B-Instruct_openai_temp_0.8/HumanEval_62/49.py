```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients where xs[0] is the constant term,
               xs[1] is the coefficient of x, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a polynomial is a new polynomial where each coefficient
    # is the derivative of the corresponding term in the original polynomial.
    # This means that the constant term is 0, and each coefficient of x is
    # multiplied by its power plus 1.
    # Therefore, we can return a new list where each element is the product
    # of the corresponding element in xs and its 1-based index.
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
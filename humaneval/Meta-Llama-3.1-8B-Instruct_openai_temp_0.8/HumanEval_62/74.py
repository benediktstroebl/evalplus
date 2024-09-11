```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial represented by its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
               The first element is the constant term, and the rest are coefficients
               of x, x^2, x^3,...

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Remove the constant term (the first element of the list) and multiply each coefficient by its index (which represents the power of x)
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
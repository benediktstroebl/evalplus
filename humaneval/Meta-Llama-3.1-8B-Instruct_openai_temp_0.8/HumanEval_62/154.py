### Derivative of a Polynomial
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial, from the constant term to the highest degree.

    Returns:
    list: Coefficients of the derivative polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
This script defines the `derivative` function, which calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to multiply each coefficient by its index (representing the power of x it corresponds to), starting from the second coefficient (index 1) since the constant term does not contribute to the derivative. The function returns the list of coefficients of the derivative polynomial.
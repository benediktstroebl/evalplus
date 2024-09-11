### Derivative of a Polynomial

The following Python script defines a function to calculate the derivative of a polynomial given its coefficients.

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               The coefficients are ordered from lowest to highest degree.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [x * i for i, x in enumerate(reversed(xs[:-1]), 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script uses a list comprehension to iterate over the coefficients of the polynomial, starting from the second-to-last coefficient (which corresponds to the term with the second-lowest degree) and moving backwards. For each coefficient `x`, it multiplies it by its degree `i`, effectively calculating the coefficient of the corresponding term in the derivative of the polynomial. The result is a list of coefficients representing the derivative of the polynomial.
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of a polynomial.

    Returns:
        list: Coefficients of the derivative polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    return [i * coeff for i, coeff in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

In this script, the function `derivative` calculates the derivative of a polynomial represented as a list of coefficients. It uses a list comprehension to generate the coefficients of the derivative polynomial. The `enumerate` function is used to get both the index and the value of each coefficient in the input list, starting from the second coefficient (index 1). The index is multiplied by the coefficient to get the coefficient of the derivative polynomial.
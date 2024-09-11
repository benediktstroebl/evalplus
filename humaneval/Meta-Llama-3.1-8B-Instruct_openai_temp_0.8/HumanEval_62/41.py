```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of the polynomial.
            The polynomial is of the form: xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
        list: A list of coefficients of the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) <= 1:
        return []
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([5]))  # []
print(derivative([]))  # []
```

This script uses a list comprehension to generate the coefficients of the derivative polynomial. The `enumerate` function is used to iterate over the coefficients and their indices. The list is sliced from index 1 to the end to exclude the constant term. The derivative of a polynomial of degree n is a polynomial of degree n-1, so the function returns an empty list if the input list contains only one or zero elements.
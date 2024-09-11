```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The polynomial is represented as xs[0] + xs[1] * x + xs[2] * x^2 +...

    Args:
        xs (list): A list of coefficients of the polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    if len(xs) <= 1:
        # If the polynomial is a constant or linear, its derivative is zero.
        return []
    return [x * i for i, x in enumerate(xs[1:], start=1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a list comprehension to generate the coefficients of the derivative of the polynomial. The `enumerate` function is used to get both the index and the value of each element in the list, and the `start=1` argument is used to make the indices start at 1 instead of 0. This is because the derivative of a constant is zero, and the derivative of a linear polynomial is the coefficient of the linear term.
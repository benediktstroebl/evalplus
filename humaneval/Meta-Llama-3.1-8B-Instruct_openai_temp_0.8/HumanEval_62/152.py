```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
    xs (list): Coefficients of the polynomial.

    Returns:
    list: Coefficients of the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:  # Handle the case where the polynomial is a constant
        return []
    return [i * x for i, x in enumerate(xs[1:], start=1)]  # Start from the second coefficient with a multiplier of 1, and so on


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: []
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It does this by multiplying each coefficient (except the first one, which is ignored) by its index, effectively applying the power rule of differentiation. If the input polynomial is a constant (i.e., it has only one coefficient), the function returns an empty list.
### Derivative of a Polynomial
#### Python Script

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The input polynomial is of the form xs[0] + xs[1] * x + xs[2] * x^2 +...
    The output polynomial is also in the same form, but its coefficients represent the
    derivative of the input polynomial.

    Args:
        xs (list): Coefficients of the input polynomial.

    Returns:
        list: Coefficients of the derivative polynomial.
    """
    if len(xs) < 2:
        return []
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([1]))  # Output: []
print(derivative([]))  # Output: []
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It uses list comprehension to generate the coefficients of the derivative polynomial. If the input polynomial has only one or zero terms, the function returns an empty list, as the derivative of a constant or the zero polynomial is zero.
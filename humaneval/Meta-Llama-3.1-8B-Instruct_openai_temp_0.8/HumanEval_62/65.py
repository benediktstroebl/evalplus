### Derivative of a Polynomial
#### Python Script

```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative of the polynomial.
    """
    if len(xs) == 1:
        return []
    else:
        # The derivative of a polynomial is calculated by multiplying each coefficient
        # by its power and reducing the power by one.
        derivative_coeffs = [i * x for i, x in enumerate(xs[1:], 1)]
        return derivative_coeffs

# Examples
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1]))  # []
print(derivative([]))  # []
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It uses a list comprehension to multiply each coefficient by its power and reduce the power by one. The function returns the coefficients of the derivative of the polynomial. If the input list has only one element, it returns an empty list, as the derivative of a constant is zero.
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial represented by a list of coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
        xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return []
    else:
        # The derivative of a polynomial is calculated by reducing the exponent of each term by 1
        # and multiplying the coefficient by the new exponent.
        return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([]))  # []
print(derivative([1]))  # []
```
This script defines a function `derivative(xs)` that calculates the derivative of a polynomial represented by a list of coefficients. It uses a list comprehension to create a new list of coefficients, where each coefficient is the product of the original coefficient and its new exponent (which is one less than the original exponent). The function also includes test cases to verify its correctness.
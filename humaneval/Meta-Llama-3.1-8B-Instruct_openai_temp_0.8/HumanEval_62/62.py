### Derivative of a Polynomial
#### Calculating the Derivative of a Polynomial in Python
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing a polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of x^n is n*x^(n-1)
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
This Python function `derivative` calculates the derivative of a polynomial, given its coefficients. The derivative of a polynomial is calculated by multiplying each coefficient by its exponent (n) and then subtracting 1 from the exponent. The `enumerate` function is used to pair each coefficient with its index (which represents the exponent), starting from 1 (since list indices start at 0).
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The coefficients are provided as a list xs where:
    - xs[0] is the constant term
    - xs[n] is the coefficient of the nth degree term

    The derivative is also given as a list of coefficients.

    For example, the derivative of 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4 is:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]

    Similarly, the derivative of 1 + 2*x + 3*x^2 is:
    >>> derivative([1, 2, 3])
    [2, 6]

    :param xs: list of coefficients of the polynomial
    :return: list of coefficients of the polynomial's derivative
    """
    return [i * x for i, x in enumerate(xs[1:], 1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1]))  # []
print(derivative([]))  # []
```

This Python script defines a function called `derivative` that takes a list of coefficients of a polynomial and returns a list of coefficients of its derivative. The function uses a list comprehension to calculate the derivative, multiplying each coefficient by its degree and ignoring the constant term.
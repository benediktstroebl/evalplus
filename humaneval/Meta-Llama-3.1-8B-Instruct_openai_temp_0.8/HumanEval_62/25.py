### Derivative of a Polynomial
#### Script

```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial.

    The input xs is a list of coefficients of a polynomial, where
    xs[i] is the coefficient of the term of degree i.

    The output is a list of coefficients of the polynomial's derivative,
    in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        # Constant polynomial
        return []
    else:
        # Remove the first element (coefficient of x^0)
        # and multiply the rest by their term's degree
        return [i * coeff for i, coeff in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1]))  # []
print(derivative([]))  # []
```
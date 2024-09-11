### Derivative of a Polynomial
#### Problem Statement

Given a list of coefficients `xs` representing a polynomial, calculate the derivative of the polynomial in the same form.

#### Solution

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] is the constant term, xs[1] is the coefficient of x,
               xs[2] is the coefficient of x^2, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_coeffs = [i * coeff for i, coeff in enumerate(xs[1:], start=1)]
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

#### Explanation

The `derivative` function uses a list comprehension to calculate the coefficients of the derivative of the polynomial. It iterates over the coefficients of the original polynomial, starting from the second coefficient (at index 1) and multiplies each coefficient by its index (i.e., the power of x it corresponds to). The result is a list of coefficients representing the derivative of the polynomial.
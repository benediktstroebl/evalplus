```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial.

    The input list xs represents the coefficients of a polynomial, where
    xs[0] is the constant term, xs[1] is the coefficient of the linear term,
    xs[2] is the coefficient of the quadratic term, and so on.

    The output is the derivative of the polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    # If the polynomial is of degree 0, its derivative is 0
    if len(xs) == 1:
        return [0]
    # Otherwise, the derivative of the polynomial is the polynomial with each term shifted by 1 position
    else:
        return [i * x for i, x in enumerate(xs[1:], 1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script first checks if the polynomial is of degree 0 (i.e., a constant). If so, it returns a list containing 0, since the derivative of a constant is 0. Otherwise, it uses a list comprehension to compute the derivative. The expression `i * x` multiplies each term by its power (which is its index `i` in the list), and the `enumerate` function generates indices and values for the list `xs` starting from 1.
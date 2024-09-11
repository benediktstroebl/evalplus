```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial

    Returns:
        list: coefficients of the derivative polynomial

    Example:
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
        return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([5]))  # Expected output: []
print(derivative([]))  # Expected output: []
```

This Python function uses list comprehension to calculate the derivative of a polynomial represented as a list of coefficients. The derivative formula is `f'(x) = n * c_n * x^(n-1)`, where `n` is the term number and `c_n` is the coefficient of the nth term in the polynomial. The function applies this formula to each term in the polynomial, excluding the constant term.
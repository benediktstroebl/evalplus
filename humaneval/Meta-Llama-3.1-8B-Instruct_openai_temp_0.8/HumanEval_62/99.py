```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients of a polynomial, where
        xs[i] is the coefficient of x^i in the polynomial.

    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    n = len(xs)
    derivative_coeffs = [i * xs[i] for i in range(1, n)]
    return derivative_coeffs

# Example usage
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

In this script, the function `derivative(xs)` calculates the derivative of a polynomial given its coefficients. The derivative of a polynomial `p(x) = a_n*x^n + a_(n-1)*x^(n-1) +... + a_1*x + a_0` is a new polynomial `p'(x) = n*a_n*x^(n-1) + (n-1)*a_(n-1)*x^(n-2) +... + a_1`. This is implemented using a list comprehension to generate the coefficients of the derivative polynomial.
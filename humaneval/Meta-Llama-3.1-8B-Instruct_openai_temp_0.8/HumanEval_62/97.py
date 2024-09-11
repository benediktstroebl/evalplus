### Derivative of a Polynomial
#### Python Script

```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    The polynomial is represented in the form: xs[0] + xs[1] * x + xs[2] * x^2 +...

    Args:
        xs (list): A list of coefficients of the polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    if len(xs) <= 1:
        return []

    derivative_coeffs = []
    for i in range(1, len(xs)):
        derivative_coeffs.append(i * xs[i])

    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The derivative of a polynomial is calculated using the power rule of differentiation, where the derivative of `x^n` is `n * x^(n-1)`. The function iterates over the coefficients of the polynomial, starting from the second coefficient (index 1), and calculates the derivative of each term by multiplying the coefficient with its power. The result is a list of coefficients of the derivative of the polynomial.
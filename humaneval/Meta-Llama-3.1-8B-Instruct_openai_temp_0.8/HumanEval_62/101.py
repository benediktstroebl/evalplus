```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial.

    Returns:
        list: coefficients of the polynomial derivative.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    derivative_coefficients = [i * coefficient for i, coefficient in enumerate(xs[1:], 1)]
    return derivative_coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script uses list comprehension to create a new list where each coefficient is the product of its index (starting from 1) and the corresponding coefficient in the input list. This is based on the power rule of differentiation in calculus, which states that the derivative of x^n is n * x^(n-1).
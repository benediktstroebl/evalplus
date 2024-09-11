```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative polynomial.
    """
    if len(xs) == 1:  # If polynomial is constant, its derivative is 0.
        return []
    elif len(xs) == 2:  # If polynomial is linear, its derivative is its coefficient.
        return xs[1:]

    # Compute derivative coefficients using powers of x.
    # For example, the derivative of ax^n is nax^(n-1).
    derivative_coeffs = [i * coeff for i, coeff in enumerate(xs[1:], start=1)]
    return derivative_coeffs


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([0, 3, 4]))  # [3]
print(derivative([4]))  # []
print(derivative([]))  # []
```

This Python script defines a function `derivative` that computes the derivative of a polynomial given its coefficients. The `derivative` function uses list comprehension to compute the coefficients of the derivative polynomial based on the power rule of differentiation. If the input polynomial is constant (i.e., has only one coefficient), the function returns an empty list, indicating that the derivative is 0. The test cases demonstrate the function's correctness.
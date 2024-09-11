```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    derivative_coeffs = [i * coeff for i, coeff in enumerate(xs[1:], start=1)]
    return derivative_coeffs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

In this script, the `derivative` function uses a list comprehension to generate the coefficients of the derivative. It iterates over the coefficients starting from the second element (index 1), multiplying each coefficient by its index (starting from 1) to get the coefficients of the derivative. The `enumerate` function is used to get the index and value of each element in the list, and the `start=1` argument is used to start the indexing from 1 instead of 0.
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    # The derivative of a polynomial is calculated by multiplying each coefficient by its exponent.
    # Then, we subtract 1 from each exponent.
    # The number of terms in the derivative polynomial will be one less than the original polynomial.
    # We use list comprehension to generate the new coefficients.
    return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script uses list comprehension to generate the coefficients of the derivative polynomial. It assumes that the input list `xs` contains coefficients in ascending order of their exponents, with the highest exponent first. The script also includes docstrings and test cases to ensure that it works correctly.
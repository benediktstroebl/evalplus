### Derivative of a Polynomial
#### A Python Function to Calculate the Derivative of a Polynomial

```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
              The polynomial is in the form xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients of the derivative of the input polynomial.
    """
    derivative_coeffs = [i * coef for i, coef in enumerate(xs[1:], 1)]
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

**How it works**:

*   We use a list comprehension to generate the coefficients of the derivative polynomial.
*   We iterate over the coefficients of the input polynomial starting from the second coefficient (`enumerate(xs[1:], 1)`), with each coefficient multiplied by its index (`i * coef`).
*   The result is a list of coefficients representing the derivative polynomial.
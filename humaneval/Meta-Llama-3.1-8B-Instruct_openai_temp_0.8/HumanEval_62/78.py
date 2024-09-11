```python
def derivative(xs: list):
    """
    Computes the derivative of a polynomial given its coefficients.

    The coefficients are assumed to be in the order:
    xs[0] + xs[1] * x + xs[2] * x^2 +... + xs[n] * x^n

    The derivative of this polynomial is:
    xs[1] + 2*xs[2]*x + 3*xs[3]*x^2 +... + n*xs[n]*x^(n-1)

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative of the polynomial.
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []

    # Iterate over the coefficients of the original polynomial
    for i in range(1, len(xs)):
        # The coefficient of x^(i-1) in the derivative is i*xs[i]
        derivative_coeffs.append(i * xs[i])

    # Return the coefficients of the derivative
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([0, 0, 0]))  # Expected output: []
```

Note: The function works by iterating over the coefficients of the original polynomial, skipping the constant term (which is represented by the first element `xs[0]`). For each remaining coefficient, it multiplies it by its index (which represents the power of x in the derivative) and adds the result to the list of coefficients of the derivative. The function then returns this list of coefficients.
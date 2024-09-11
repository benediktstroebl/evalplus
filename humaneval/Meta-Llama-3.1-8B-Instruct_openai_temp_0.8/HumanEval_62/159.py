```python
def derivative(xs: list):
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial
        xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative polynomial in the same form.
    """
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return []
    else:
        # Derivative of a polynomial is a new polynomial where each coefficient
        # is the product of the original coefficient and its index, and then
        # we shift the polynomial down by one degree. This is equivalent to
        # multiplying the original polynomial by (x+1) and then dividing by x.
        return [i * coef for i, coef in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Expected output: [2, 6]
```

This script implements the `derivative` function according to the provided specification. The function takes a list of coefficients `xs` representing the polynomial, and returns the coefficients of the derivative polynomial in the same form. The test cases at the end demonstrate the function's correctness.
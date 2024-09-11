```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of a polynomial.
            xs[0] is the coefficient of x^0 (constant term),
            xs[1] is the coefficient of x^1,
            xs[2] is the coefficient of x^2, and so on.

    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    derivative_coefficients = []
    for i in range(1, len(xs)):
        # Coefficient of x^(n-1) in the derivative is n * coefficient of x^n in the original polynomial
        derivative_coefficients.append(i * xs[i])
    return derivative_coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function called `derivative` which takes a list of coefficients as input and returns a list of coefficients of the derivative polynomial. It then tests this function with the provided test cases. The code follows the docstring and comments to explain each part of the code.
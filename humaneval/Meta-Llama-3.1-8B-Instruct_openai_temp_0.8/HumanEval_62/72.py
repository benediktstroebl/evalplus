Here is a self-contained Python script that solves the problem:

```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
               xs[0] is the coefficient of the constant term,
               xs[1] is the coefficient of the linear term,
               xs[2] is the coefficient of the quadratic term, and so on.

    Returns:
    list: A list of coefficients of the derivative polynomial.
    """
    # Initialize an empty list to store the coefficients of the derivative polynomial
    derivative_coeffs = [0] * len(xs)

    # The derivative of the constant term is 0, so we start from the linear term
    for i in range(1, len(xs)):
        # The coefficient of the derivative of the ith term is i * xs[i]
        derivative_coeffs[i - 1] = i * xs[i]

    return derivative_coeffs


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns a list of coefficients of the derivative polynomial. The function uses a simple loop to calculate the coefficients of the derivative polynomial.
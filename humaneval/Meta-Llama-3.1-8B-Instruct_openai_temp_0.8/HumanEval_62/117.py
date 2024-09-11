```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.

    The input is a list of coefficients, where the first element represents the constant term,
    the second element represents the coefficient of x, the third element represents the coefficient of x^2, and so on.

    The function returns a new list containing the coefficients of the derivative polynomial.

    :param xs: A list of coefficients of the polynomial.
    :return: A list of coefficients of the derivative polynomial.
    """
    # Ensure the input list is not empty
    if not xs:
        raise ValueError("The input list cannot be empty.")

    # The derivative of a constant term is zero, so we return an empty list for the constant term
    derivative_xs = [0] if len(xs) == 1 else []

    # The derivative of x^n is n * x^(n-1), so we calculate the coefficients of the derivative polynomial
    for i in range(1, len(xs)):
        # The coefficient of x^(n-1) is i * xs[i]
        derivative_xs.append(i * xs[i])

    return derivative_xs


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to calculate the coefficients of the derivative polynomial. The example usage demonstrates how to use the function to calculate the derivatives of two polynomials.
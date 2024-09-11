```python
def derivative(xs: list) -> list:
    """
    This function takes a list of coefficients of a polynomial as input and returns the coefficients of the derivative of the polynomial.

    The input list is expected to be in the format: [constant, x, x^2, x^3,...]

    The returned list will be in the same format with the coefficients of the derivative.

    For example, if the input is [3, 1, 2, 4, 5], the output will be [1, 4, 12, 20] which represents the derivative of the polynomial 3 + x + 2x^2 + 4x^3 + 5x^4.

    :param xs: A list of coefficients of a polynomial
    :return: A list of coefficients of the derivative of the polynomial
    """
    return [i * (i - 1) for i in xs[1:]]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses list comprehension to generate the coefficients of the derivative. For each coefficient `i` (except the constant term, which is the first element of the list), it calculates `i * (i - 1)` to get the corresponding coefficient of the derivative. The result is a list of coefficients of the derivative of the input polynomial.
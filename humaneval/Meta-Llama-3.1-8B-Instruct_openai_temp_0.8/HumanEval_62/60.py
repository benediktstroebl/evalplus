Here is a well-documented Python script that implements the derivative function:
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The input list represents the coefficients of the polynomial in ascending order of degree.
    For example, the polynomial 3 + 2x + 4x^2 + 5x^3 is represented as [3, 2, 4, 5].

    The function returns the coefficients of the derivative polynomial.

    :param xs: List of coefficients of the polynomial
    :return: List of coefficients of the derivative polynomial
    """
    derivative_coeffs = [i * coeff for i, coeff in enumerate(xs[1:], start=1)]
    return derivative_coeffs


# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script uses a list comprehension to calculate the coefficients of the derivative polynomial. The `enumerate` function is used to iterate over the input list `xs` with both the index `i` and the value `coeff`. The `start=1` argument is used to start the index at 1, as the derivative of the constant term is 0.

The script then returns the list of derivative coefficients. The example usage demonstrates how the function can be used to calculate the derivative of polynomials with different coefficients.
### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The polynomial is represented as:
    xs[0] + xs[1] * x + xs[2] * x^2 +...

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative of the polynomial.
    """
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients `xs` and returns a new list containing the coefficients of the derivative of the polynomial. The function uses a list comprehension to multiply each non-zero coefficient (starting from the second one) by its index plus one, effectively calculating the derivative.
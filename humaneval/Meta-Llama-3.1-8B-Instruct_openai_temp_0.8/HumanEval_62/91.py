### Python Script to Calculate the Derivative of a Polynomial
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing the polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Remove the first element (constant term) as derivative of constant term is 0
    return [i * x for x, i in enumerate(xs[1:], 1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script uses list comprehension to generate the coefficients of the derivative polynomial. It iterates over the input polynomial coefficients (excluding the constant term), multiplying each by its corresponding power of `x` (i.e., the index plus one). The resulting list of coefficients represents the derivative polynomial.
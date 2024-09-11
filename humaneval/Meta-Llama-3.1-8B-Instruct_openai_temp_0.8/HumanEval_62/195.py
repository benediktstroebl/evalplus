```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Handle polynomials of degree 0 (e.g. constant functions)
    if len(xs) == 1:
        return []
    
    # Derivative of a polynomial is calculated by shifting coefficients and multiplying by their indices (except for the first one)
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial, calculates the derivative of the polynomial, and returns the coefficients of the derivative as a list. It handles polynomials of degree 0 (constant functions) by returning an empty list. The function uses a list comprehension with `enumerate` to calculate the coefficients of the derivative. The example usage demonstrates how to use the `derivative` function with different input polynomials.
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial.

    Args:
    xs: A list of coefficients of a polynomial.
        xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    The derivative of the polynomial in the same form.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Start from the second coefficient (index 1) since derivative of a
    # constant term is 0.
    return [i * xs[i] for i in range(1, len(xs))]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns the derivative of the polynomial in the same form. It uses a list comprehension to compute the derivative, multiplying each coefficient by its index (since the derivative of `x^n` is `n*x^(n-1)`). The function starts from the second coefficient (index 1) since the derivative of a constant term is 0.
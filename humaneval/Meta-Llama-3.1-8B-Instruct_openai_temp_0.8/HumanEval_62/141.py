```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.
        The polynomial is in the form xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative polynomial.
    """
    # The derivative of a polynomial is computed by multiplying each coefficient by its power (except the constant term) and decreasing the power by one.
    # We use a list comprehension to create the new list of coefficients.
    # The formula for the derivative of a term is 'power * coefficient'.
    # We ignore the first (constant) term since it has a power of zero.
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

The code defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns the coefficients of the derivative polynomial. It uses a list comprehension to create the new list of coefficients by multiplying each coefficient (except the constant term) by its power (which is its index in the list minus one) and decreasing the power by one. The example usage shows how to call the function with different inputs.
```python
def derivative(xs: list):
    """
    Returns the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Remove the leading coefficient (since it's 0 in the derivative)
    # and multiply every other coefficient by its index + 1
    return [i * coefficient for i, coefficient in enumerate(xs[1:], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to create a new list where each coefficient is multiplied by its index + 1, effectively calculating the derivative of the polynomial. The `enumerate` function is used to get both the index and value of each coefficient in the input list, starting from the second coefficient (index 1) since the first coefficient is the constant term which is zero in the derivative.
### Derivative of a Polynomial
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return []
    else:
        # For each coefficient, multiply by its power (index + 1) and subtract its index
        return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

In this script, we assume that the input is a list of coefficients representing a polynomial in descending order of powers. The function uses a list comprehension to calculate the coefficients of the derivative polynomial. If the input list has only one element, it returns an empty list, as the derivative of a constant is zero.
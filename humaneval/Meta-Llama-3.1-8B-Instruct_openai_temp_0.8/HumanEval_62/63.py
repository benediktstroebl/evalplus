### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing a polynomial.
              The first element is the constant term, and subsequent elements
              are the coefficients of ascending powers of x.

    Returns:
    list: A list of coefficients representing the derivative of the input polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of that polynomial. The function uses a list comprehension to create the new list of coefficients, where each coefficient is the product of its original index (plus one, to account for zero-based indexing) and its original value.
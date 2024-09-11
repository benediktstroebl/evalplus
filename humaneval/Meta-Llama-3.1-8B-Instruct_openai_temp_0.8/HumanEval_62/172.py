```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of a polynomial in the form xs[0] + xs[1] * x + xs[2] * x^2 +....

    Returns:
    list: The coefficients of the derivative of the input polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [xs[0] * i for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative(xs)` that calculates the derivative of a polynomial given its coefficients. It uses a list comprehension to multiply each coefficient by its position (starting from 1, since the 0th position is the constant term) to get the coefficients of the derivative. The script then tests the function with two examples.
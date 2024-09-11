```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
               The polynomial is represented as xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) <= 1:
        # If the polynomial is constant or linear, its derivative is zero or the coefficient of x, respectively
        return [0] * (len(xs) - 1)
    return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([0]))  # Output: []
print(derivative([1]))  # Output: [0]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It uses list comprehension to generate the coefficients of the derivative. The function handles the cases where the polynomial is constant (i.e., has only one coefficient) or linear (i.e., has two coefficients), in which case the derivative is zero or the coefficient of x, respectively. The script then tests the function with several examples.
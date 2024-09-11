```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               The coefficients are in the order of the polynomial:
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a constant is 0
    if len(xs) == 1:
        return [0]
    # The derivative of x^n is n * x^(n-1)
    else:
        return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

In this script, the `derivative` function calculates the derivative of a polynomial represented as a list of coefficients. The function uses a list comprehension to multiply each coefficient by its index (which represents the power of x) and returns the resulting list. If the input list has only one element (i.e., it represents a constant polynomial), the function returns a list containing zero, since the derivative of a constant is zero.
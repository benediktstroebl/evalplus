```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): A list of coefficients of a polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` and returns a list of coefficients representing the derivative of the polynomial. It uses a list comprehension to generate the coefficients of the derivative, where each coefficient is the product of its original coefficient and its power (i.e., its index in the list minus one, starting from zero). The `enumerate` function is used to get the index and value of each element in the list.

For example, if the input list is `[3, 1, 2, 4, 5]`, the output list will be `[1, 4, 12, 20]`, which are the coefficients of the polynomial `1 + 4x + 12x^2 + 20x^3`.
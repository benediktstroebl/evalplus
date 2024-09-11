```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return []
    else:
        return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

This script defines a function `derivative` that calculates the derivative of a polynomial represented as a list of coefficients. It uses list comprehension to generate the coefficients of the derivative polynomial. The time complexity of this function is O(n), where n is the number of coefficients in the polynomial. The space complexity is also O(n).
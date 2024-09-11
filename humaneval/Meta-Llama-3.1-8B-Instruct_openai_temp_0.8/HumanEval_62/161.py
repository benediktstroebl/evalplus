### Derivative of a Polynomial
#### Python Script
```markdown
### derivative.py
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial in ascending order of x's power.

    Returns:
    list: Coefficients of the derivative polynomial in ascending order of x's power.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_xs = [i * coefficient for i, coefficient in enumerate(xs[1:], 1)]
    return derivative_xs


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

### Explanation
The script defines a function `derivative` that takes a list of coefficients `xs` as input. It uses list comprehension to calculate the derivative of the polynomial. The `enumerate` function is used to get both the index and the value of each element in the list, starting from the second element (index 1) because the power of the first term is 0 and its derivative is 0.

### Testing
The script includes doctest to verify the correctness of the function. You can run the script to test it.
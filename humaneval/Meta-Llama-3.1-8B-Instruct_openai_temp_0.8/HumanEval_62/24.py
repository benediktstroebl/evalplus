```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of the polynomial. xs[i] is the coefficient of x^i.
    
    Returns:
    list: A list of coefficients of the derivative polynomial.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The coefficients of the derivative polynomial are calculated by multiplying each coefficient in xs by its index and then subtracting the index-1 times the coefficient of the term of one less degree.
    return [i * x for i, x in enumerate(xs[:-1], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script uses Python's built-in list comprehension feature to calculate the coefficients of the derivative polynomial. The `enumerate` function is used to get both the index and value of each element in the `xs` list. The `[:-1]` slice is used to exclude the last element (which is the constant term and doesn't have a derivative). The `1` as the second argument to `enumerate` is used to start the index at 1 instead of 0.
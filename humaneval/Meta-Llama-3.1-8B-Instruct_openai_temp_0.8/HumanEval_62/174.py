```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): List of coefficients of a polynomial, 
              where xs[i] is the coefficient of x^i.

    Returns:
    list: List of coefficients of the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Output: [2, 6]
```

This function uses list comprehension to calculate the derivative of the polynomial. The `enumerate` function is used to get both the index and the value of each element in the list, starting from the second element (index 1). The index is then multiplied by the corresponding coefficient to get the coefficient of the derivative.

Note: This function assumes that the input list represents a polynomial with non-zero leading coefficient. If the input list represents a polynomial with zero leading coefficient (i.e., a constant), the function will return an empty list. If you want to handle this case differently, you can modify the function accordingly.
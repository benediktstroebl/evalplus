```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    
    # If the polynomial is constant (i.e., it has only one term), its derivative is 0
    if len(xs) == 1:
        return [0]
    
    # The derivative of a polynomial is calculated by multiplying each term by its exponent and subtracting one from its exponent
    return [x * i for i, x in enumerate(xs[1:], start=1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` as input and returns the list of coefficients of the derivative of the polynomial represented by `xs`. The function uses list comprehension to calculate the derivative of the polynomial. If the input polynomial is constant (i.e., it has only one term), the function returns `[0]` as the derivative is 0. The script includes test cases to verify the correctness of the function.
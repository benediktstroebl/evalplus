```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients representing a polynomial.
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:  # base case for polynomials of degree 0
        return []
    
    n = len(xs) - 1  # degree of the polynomial
    derivative_coefficients = [i * xs[i] for i in range(1, n + 1)]  # derivative formula: derivative of x^n = n*x^(n-1)
    
    return derivative_coefficients

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # expected output: [2, 6]
```
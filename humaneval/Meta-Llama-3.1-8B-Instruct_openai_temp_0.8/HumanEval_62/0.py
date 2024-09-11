```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of a polynomial. 
               The index of each coefficient represents the power of x it corresponds to.
               For example, if xs = [3, 1, 2, 4, 5], then the polynomial is 3 + x + 2x^2 + 4x^3 + 5x^4.
    
    Returns:
    list: The coefficients of the derivative of the polynomial.
    """
    
    # Remove the coefficients of the terms with power 0, because they don't contribute to the derivative
    xs = xs[1:]
    
    # The derivative of x^n is n*x^(n-1)
    # So, we multiply each coefficient by its power (which is its index) and subtract one from the power
    derivative_coefficients = [i * x for i, x in enumerate(xs, start=1)]
    
    return derivative_coefficients

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients of a polynomial and returns the coefficients of its derivative. The function uses a list comprehension to calculate the derivative coefficients. It multiplies each coefficient by its power (which is its index) and subtracts one from the power to get the derivative coefficient. The function then returns the list of derivative coefficients. The script also includes test cases to demonstrate the function's correctness.
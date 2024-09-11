```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
        xs (list): A list of coefficients of a polynomial. 
                   xs[0] is the coefficient of x^0, xs[1] is the coefficient of x^1, and so on.
    
    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    
    # If the polynomial is of degree 0 (i.e., a constant), its derivative is zero.
    if len(xs) == 1:
        return []
    
    # Initialize an empty list to store the coefficients of the derivative.
    derivative_coeffs = [0] * (len(xs) - 1)
    
    # The derivative of x^n is n*x^(n-1).
    # So, we multiply each coefficient in xs by its index and store it in derivative_coeffs.
    for i in range(1, len(xs)):
        derivative_coeffs[i - 1] = i * xs[i]
    
    # Return the list of coefficients of the derivative.
    return derivative_coeffs

# Test the function.
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function iterates over the coefficients, starting from the second one (index 1), and multiplies each coefficient by its index to get the coefficient of the corresponding power in the derivative. It returns the list of coefficients of the derivative.
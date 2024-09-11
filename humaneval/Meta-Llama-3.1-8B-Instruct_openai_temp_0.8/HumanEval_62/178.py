```python
def derivative(xs: list):
    """ 
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
        xs (list): A list of coefficients of the polynomial in ascending order of powers.
                  For example, for the polynomial 3 + 2x + x^2 + 4x^3 + 5x^4, xs would be [3, 2, 1, 4, 5].
    
    Returns:
        list: A list of coefficients of the derivative of the polynomial.
              For example, for the polynomial 3 + 2x + x^2 + 4x^3 + 5x^4, the derivative is 2 + 2x + 12x^2 + 20x^3.
    """
    
    # The derivative of x^n is n*x^(n-1)
    # So, we multiply each coefficient by its power
    derivative_coeffs = [i * x for i, x in enumerate(xs) if i!= 0]
    
    return derivative_coeffs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Expected output: [2, 6]
```

This script uses Python's list comprehension feature to create a new list `derivative_coeffs` where each coefficient is multiplied by its power (its index in the list, with the first element considered to be 0th power). The condition `if i!= 0` is used to ignore the constant term (which is the first element in the list).
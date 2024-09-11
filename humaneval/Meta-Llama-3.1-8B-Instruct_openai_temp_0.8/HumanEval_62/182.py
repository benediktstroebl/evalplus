```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    The polynomial is represented as a list of coefficients, where the index of the list 
    represents the power of the variable (x) and the value at that index is the coefficient.
    
    For example, the polynomial 3 + 1 * x + 2 * x^2 + 4 * x^3 + 5 * x^4 would be represented 
    as [3, 1, 2, 4, 5].
    
    The function returns the list of coefficients representing the derivative of the polynomial.
    
    Parameters:
    xs (list): The coefficients of the polynomial.
    
    Returns:
    list: The coefficients of the derivative of the polynomial.
    """
    
    # If the polynomial is constant (i.e., it has no variable), its derivative is 0
    if len(xs) == 1:
        return [0]
    
    # The derivative of a polynomial is calculated by multiplying each coefficient by its power
    # and then subtracting the power of the next coefficient times the current coefficient
    return [(i+1)*xs[i] for i in range(len(xs)-1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([1]))  # Output: [0]
```
### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial.
    
    The polynomial is represented by a list of coefficients, where the first element represents the constant term, 
    the second element represents the coefficient of x, the third element represents the coefficient of x^2, and so on.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
    
    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    
    # If the polynomial is a constant, its derivative is 0
    if len(xs) == 1:
        return []
    
    # Initialize the list to store the coefficients of the derivative polynomial
    derivative_xs = []
    
    # For a polynomial of degree n, the derivative will be of degree (n-1)
    # So, we start from the second coefficient (index 1) and multiply each coefficient by its index
    for i in range(1, len(xs)):
        # Calculate the coefficient of the derivative polynomial
        derivative_xs.append(i * xs[i])
    
    return derivative_xs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([5]))  # Expected output: []
```
```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients representing a polynomial.
              For example, [3, 1, 2, 4, 5] represents the polynomial 3 + x + 2x^2 + 4x^3 + 5x^4.
    
    Returns:
    list: A list of coefficients representing the derivative of the given polynomial.
    """
    
    # If the polynomial is a constant (i.e., has no x term), return [0]
    if len(xs) == 1:
        return [0]
    
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []
    
    # The coefficient of the x term in the derivative is the coefficient of the x^2 term in the original polynomial
    derivative_coeffs.append(xs[1])
    
    # For each coefficient of the polynomial starting from the x^2 term
    for i in range(2, len(xs)):
        # The coefficient of the x^(i-1) term in the derivative is i times the coefficient of the x^i term in the original polynomial
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: [0]
print(derivative([1]))  # Output: [0]
```
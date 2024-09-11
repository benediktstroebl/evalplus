```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    The input xs is a list of coefficients, where xs[0] is the constant term,
    xs[1] is the coefficient of the linear term, xs[2] is the coefficient of the quadratic term, and so on.
    
    The function returns a new list representing the coefficients of the derivative of the polynomial.
    
    Example usage:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if the input list has at least two elements
    if len(xs) < 2:
        raise ValueError("The input list must have at least two elements.")
    
    # Create a new list to store the coefficients of the derivative
    # The derivative of x^n is n*x^(n-1)
    # So, the coefficient of x^(n-1) is n times the coefficient of x^n
    derivative_xs = []
    
    # Iterate over the coefficients of the original polynomial, starting from the second coefficient
    for i in range(1, len(xs)):
        # Calculate the coefficient of the derivative by multiplying the original coefficient with its index
        coefficient = i * xs[i]
        # Append the calculated coefficient to the list of derivative coefficients
        derivative_xs.append(coefficient)
    
    # Return the list of derivative coefficients
    return derivative_xs

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

This script defines a function `derivative` that takes a list of coefficients as input and returns a new list representing the coefficients of the derivative of the polynomial. The function iterates over the coefficients of the original polynomial, starting from the second coefficient, and calculates the corresponding coefficient of the derivative by multiplying the original coefficient with its index. The function then returns the list of derivative coefficients.
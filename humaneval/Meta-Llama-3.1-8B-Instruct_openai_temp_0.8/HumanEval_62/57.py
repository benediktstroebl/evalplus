```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] is the constant term, xs[1] is the coefficient of x, 
               xs[2] is the coefficient of x^2, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # If the polynomial is constant, its derivative is zero
    if len(xs) == 1:
        return []
    
    # Initialize the result list with the derivative of the constant term (which is zero)
    result = []
    
    # Calculate the derivative of each term
    # The derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2)
    # So, the coefficient of the derivative is i * xs[i]
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    
    return result

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script uses a simple iterative approach to calculate the derivative of each term in the polynomial, based on the power rule of differentiation. The result is a list of coefficients representing the derivative of the polynomial.
```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    The polynomial is represented as a list of coefficients, where the first coefficient is the constant term, 
    and each subsequent coefficient represents the coefficient of the corresponding power of x.

    Parameters:
    xs (list): A list of coefficients representing the polynomial.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_xs = []
    
    # The derivative of x^n is n * x^(n-1), so we multiply each coefficient by its index and add it to the list
    # We only include coefficients for powers of x greater than 1, so we start at index 1
    for i in range(1, len(xs)):
        # Multiply the coefficient by its index
        coefficient_derivative = i * xs[i]
        
        # Add the coefficient of the derivative to the list
        derivative_xs.append(coefficient_derivative)
    
    # Return the list of coefficients representing the derivative
    return derivative_xs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. The function uses a loop to calculate the derivative of each term in the polynomial, and it returns the list of coefficients representing the derivative. The example usage at the end demonstrates how to use the function.
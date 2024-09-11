```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    The coefficients of the polynomial are represented in the list xs.
    The coefficients are in the order of the highest power of x to the lowest power of x.
    xs[0] + xs[1] * x + xs[2] * x^2 +... 
    The derivative is calculated based on the power rule of differentiation.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
    
    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coefficients = []
    
    # Iterate over the coefficients in the polynomial, starting from the second coefficient (index 1)
    for i in range(1, len(xs)):
        # The derivative of a term with power n is n * xs[n]
        # So, we multiply the coefficient of the term by its power (i)
        # and append the result to the list of derivative coefficients
        derivative_coefficients.append(i * xs[i])
    
    # Return the list of derivative coefficients
    return derivative_coefficients

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. The function uses a loop to calculate the derivative of each term in the polynomial, and the result is returned as a list of coefficients. The example usage at the end shows how to use the function to calculate the derivative of two different polynomials.
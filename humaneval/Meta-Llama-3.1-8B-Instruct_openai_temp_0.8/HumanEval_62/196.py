```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of a polynomial. 
               xs[0] is the constant term, xs[1] is the coefficient of x, and so on.
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    
    # We start with an empty list to store the coefficients of the derivative
    derivative_xs = []
    
    # We iterate over the coefficients of the original polynomial, starting from the second coefficient (index 1)
    for i in range(1, len(xs)):
        # For each coefficient, we multiply it by its exponent (which is its index) and add it to the list
        # This is because the derivative of a term x^n is n*x^(n-1)
        derivative_xs.append(i * xs[i])
    
    # Finally, we return the list of coefficients of the derivative
    return derivative_xs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([1]))  # Expected output: []
print(derivative([]))  # Expected output: []
```

This script defines a function `derivative` that takes a list of coefficients as input and returns the list of coefficients of the derivative of the polynomial. The function uses a simple loop to calculate the coefficients of the derivative, which are obtained by multiplying each coefficient by its exponent (its index in the list) and adding it to a new list. The function is then tested with several example inputs.
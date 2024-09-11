```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    
    The input coefficients are of the form xs = [a, b, c, d, e,...]
    where the polynomial is a + bx + cx^2 + dx^3 + ex^4 +...
    
    The output is the derivative of the polynomial in the same form.
    
    Parameters:
    xs (list): A list of coefficients of the polynomial.
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    # Remove leading zeros
    xs = [x for x in xs if x!= 0]
    
    # Calculate the derivative of the polynomial
    # The derivative of ax^n is nx^(n-1)
    derivative_coeffs = [i * x for i, x in enumerate(xs[1:], start=1)]
    
    return derivative_coeffs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([0, 0, 0, 0, 1]))  # Expected output: [0, 0, 0]
```

This script defines a function `derivative` that calculates the derivative of a polynomial. It removes leading zeros from the input coefficients and then calculates the derivative by multiplying each coefficient with its power (starting from 1). The function returns the list of coefficients of the derivative of the polynomial. The test cases at the end demonstrate the usage of the function.
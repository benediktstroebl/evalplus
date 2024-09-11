```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial.
    
    Parameters:
    xs (list): A list of coefficients representing a polynomial.
               The polynomial is in the form: xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients representing the derivative of the input polynomial.
    """
    
    # If the list is empty, return an empty list because the derivative of a constant is zero.
    if not xs:
        return []
    
    # Initialize an empty list to store the coefficients of the derivative.
    derivative_coeffs = [0] * (len(xs) - 1)
    
    # Calculate the coefficients of the derivative.
    for i in range(1, len(xs)):
        derivative_coeffs[i - 1] = i * xs[i]
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```
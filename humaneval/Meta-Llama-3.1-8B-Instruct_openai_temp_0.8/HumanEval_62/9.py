### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a given polynomial.
    
    Args:
    xs (list): A list of coefficients representing a polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    
    # Check if the input list is empty
    if len(xs) == 1:
        return []

    # Initialize an empty list to store the derivative's coefficients
    derivative_coeffs = []
    
    # Calculate the derivative's coefficients
    for i in range(1, len(xs)):
        # The derivative of x^n is n * x^(n-1)
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs


# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of that polynomial. The function uses a for loop to calculate the derivative's coefficients based on the power rule of differentiation (i.e., the derivative of x^n is n * x^(n-1)).
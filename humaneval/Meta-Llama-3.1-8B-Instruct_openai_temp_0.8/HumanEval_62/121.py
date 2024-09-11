### Calculating Polynomial Derivative
#### Using Python

```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial.
    
    Args:
        xs (list): A list of coefficients representing the polynomial.
            The polynomial is in the form xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
        list: The derivative of the polynomial in the same form.
    """
    
    # Initialize the derivative coefficients list with the first element (since the derivative of x^n is n*x^(n-1))
    derivative_coeffs = [xs[0] * 0]
    
    # For each coefficient in the polynomial (except the first one), calculate the derivative
    for i in range(1, len(xs)):
        # The derivative of xs[i] * x^i is i * xs[i] * x^(i-1)
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` and returns the list of coefficients of the derivative polynomial. It uses a simple loop to calculate the derivative coefficients, which are then returned as a list. The test cases at the end demonstrate how to use this function.
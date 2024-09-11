```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial. The first element is the constant term, 
               the second element is the coefficient of x, the third element is the coefficient of x^2, and so on.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    
    # Create a new empty list to store the coefficients of the derivative
    derivative_coeffs = []
    
    # The derivative of the constant term is 0, so we start from the second element
    for i in range(1, len(xs)):
        # The derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2), so we multiply by i
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

In this code, we define a function `derivative` that takes a list of coefficients as input and returns a new list representing the coefficients of the derivative of the polynomial. The function uses a loop to calculate the coefficients of the derivative, starting from the second element of the input list (since the derivative of the constant term is 0). The function then returns the list of coefficients. The test cases at the end demonstrate the use of the function with two different polynomials.
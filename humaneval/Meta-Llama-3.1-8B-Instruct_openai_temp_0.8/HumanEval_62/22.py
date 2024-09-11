```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients representing a polynomial in the form of xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients representing the derivative of the input polynomial.
    """
    # Check if the input is a list
    if not isinstance(xs, list):
        raise TypeError("Input must be a list of coefficients.")
    
    # Check if the list has at least one element
    if len(xs) < 1:
        raise ValueError("Input list must have at least one element.")
    
    # Check if all elements in the list are numbers
    if not all(isinstance(x, (int, float)) for x in xs):
        raise ValueError("All coefficients must be numbers.")
    
    # Calculate the derivative by shifting coefficients and multiplying by the current power
    derivative_coefficients = [i * x for i, x in enumerate(xs[1:], start=1)]
    
    return derivative_coefficients

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function takes a list of coefficients as input, checks for valid input, and returns a list of coefficients representing the derivative of the input polynomial. The test cases at the end demonstrate the function's usage.
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of the polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The coefficients of the derivative polynomial.
    """
    # If the polynomial is a constant (only one coefficient), its derivative is zero.
    if len(xs) == 1:
        return []
    
    # Initialize an empty list to store the coefficients of the derivative polynomial.
    derivative_coefficients = []
    
    # For each coefficient, multiply it by its exponent (which is its index in the list) and add it to the result.
    for i in range(1, len(xs)):
        # The exponent is i, so we multiply the coefficient by i.
        derivative_coefficients.append(xs[i] * i)
    
    return derivative_coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns the coefficients of the derivative polynomial. It uses a simple loop to calculate the derivative coefficients by multiplying each coefficient by its exponent and adding it to the result. The test cases at the end demonstrate the function's usage.
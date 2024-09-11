```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    
    # Initialize an empty list to store the coefficients of the derivative.
    derivative_coefficients = []
    
    # Iterate over the coefficients of the polynomial starting from the second one (index 1).
    for i in range(1, len(xs)):
        # For each coefficient, its corresponding coefficient in the derivative is the coefficient times its exponent.
        # So, we multiply the coefficient by its exponent (i) and append it to the list.
        derivative_coefficients.append(xs[i] * i)
    
    # Return the list of coefficients of the derivative.
    return derivative_coefficients


# Test the function with some examples.
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1, 2]))  # [2]
print(derivative([1]))  # []
```

This script defines a function `derivative(xs)` that calculates the derivative of a polynomial given its coefficients. It uses a loop to multiply each coefficient by its exponent and returns the resulting list of coefficients.
```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients representing the polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
          If the input polynomial is a constant, an empty list is returned.
    """
    
    # Check if the input polynomial is a constant (only one coefficient)
    if len(xs) == 1:
        return []
    
    # Calculate the derivative of the polynomial by multiplying each coefficient by its power
    # and then subtracting one from the power
    derivative_coefficients = [i * coefficient for i, coefficient in enumerate(xs[1:], start=1)]
    
    return derivative_coefficients


# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: []
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial as input and returns a list of coefficients representing the derivative of the polynomial. The function uses list comprehension to calculate the derivative coefficients by multiplying each coefficient by its power and then subtracting one from the power. If the input polynomial is a constant, the function returns an empty list. The example usage demonstrates how to use the function with different input polynomials.
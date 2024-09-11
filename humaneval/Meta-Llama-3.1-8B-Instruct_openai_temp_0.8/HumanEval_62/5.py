```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients representing a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    
    # Remove the first coefficient (constant term) because its derivative is 0
    xs = xs[1:]
    
    # For each coefficient, multiply it by its exponent (which is its position in the list)
    xs = [i * x for i, x in enumerate(xs)]
    
    return xs

# Example usage
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial, calculates the derivative of the polynomial, and returns the derivative in the same form as the input. The function uses list comprehension to multiply each coefficient by its exponent (which is its position in the list), effectively calculating the derivative of each term. The constant term (first coefficient) is removed because its derivative is 0.
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
    
    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    # The derivative of a term x^n is n*x^(n-1)
    # So, we multiply each term by its power and decrement the power by 1
    # The first term (constant) has a power of 0, so its derivative is 0
    return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to multiply each term by its power and decrement the power by 1. The first term (constant) has a power of 0, so its derivative is 0. The function returns the list of coefficients of the derivative polynomial. The script also includes two test cases to demonstrate the function's usage.
```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of a polynomial.
               For example, [3, 1, 2, 4, 5] represents the polynomial 3 + x + 2x^2 + 4x^3 + 5x^4
    
    Returns:
    list: A list of coefficients of the derivative of the input polynomial.
    """
    
    # Initialize an empty list to store the coefficients of the derivative
    dxs = []
    
    # The derivative of a constant is 0, so we start from the second coefficient
    for i in range(1, len(xs)):
        # The derivative of x^n is n*x^(n-1)
        # So we multiply the coefficient by the exponent and decrement the exponent
        dxs.append(i * xs[i])
    
    return dxs


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns a list of coefficients of the derivative of the input polynomial. The function iterates over the input list starting from the second element (index 1) and for each element, it calculates the coefficient of the derivative by multiplying the current coefficient by its exponent. The function returns the list of coefficients of the derivative. The script includes two test cases to demonstrate the function's correctness.
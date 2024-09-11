```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    The polynomial is represented as a list of coefficients, where the first element 
    corresponds to the constant term, the second element corresponds to the coefficient 
    of the x term, the third element corresponds to the coefficient of the x^2 term, 
    and so on.
    
    The derivative is also represented as a list of coefficients.
    
    Parameters:
    xs (list): The coefficients of the polynomial.
    
    Returns:
    list: The coefficients of the derivative of the polynomial.
    """
    # If the list has only one element, return an empty list because 
    # the derivative of a constant is zero.
    if len(xs) == 1:
        return []
    
    # Initialize an empty list to store the coefficients of the derivative.
    derivative_coefficients = []
    
    # For each coefficient in the list, multiply it by its index and add it to the 
    # list of derivative coefficients. The index represents the exponent of the 
    # corresponding term in the polynomial.
    for i in range(1, len(xs)):
        derivative_coefficients.append(xs[i] * i)
    
    return derivative_coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function iterates over the coefficients, starting from the second one (index 1), and multiplies each coefficient by its index to get the corresponding coefficient in the derivative. If the input list has only one element, the function returns an empty list, because the derivative of a constant is zero. The script includes two test cases to demonstrate the function's correctness.
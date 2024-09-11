```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a given polynomial.
    
    Parameters:
    xs (list): coefficients of the polynomial in descending order of power.
    
    Returns:
    list: coefficients of the derivative polynomial in descending order of power.
    """
    
    # If the list has one or zero elements, return an empty list
    if len(xs) <= 1:
        return []
    
    # Initialize an empty list to store the derivative coefficients
    derivative_coefficients = []
    
    # Iterate over the coefficients of the original polynomial
    for i in range(1, len(xs)):
        # Calculate the coefficient of the derivative by multiplying the current coefficient
        # with its power and subtracting the power
        derivative_coefficients.append(i * xs[i])
    
    return derivative_coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This Python script defines a function called `derivative` that takes a list of coefficients representing a polynomial and returns a new list of coefficients representing the derivative of the polynomial. The function uses a loop to calculate the derivative coefficients based on the power of each term in the original polynomial. If the input list has one or zero elements, the function returns an empty list.
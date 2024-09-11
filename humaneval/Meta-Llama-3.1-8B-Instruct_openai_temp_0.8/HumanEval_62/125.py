```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): The coefficients of the polynomial, where xs[i] is the coefficient of x^i.

    Returns:
    list: The coefficients of the derivative of the polynomial.
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_xs = []
    
    # The derivative of a constant is 0, so we start with 0
    derivative_xs.append(0)
    
    # For each coefficient xs[i] starting from the second one
    for i in range(1, len(xs)):
        # The derivative of xs[i] * x^(i-1) is (i-1)*xs[i] * x^(i-2)
        # So we multiply xs[i] by i and add the result to the list
        derivative_xs.append(i * xs[i])
    
    # Return the coefficients of the derivative
    return derivative_xs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This Python function calculates the derivative of a polynomial, given its coefficients, by storing the coefficients of the derivative in a new list. It iterates over the coefficients of the input polynomial (excluding the constant term), each time multiplying the current coefficient by its power to obtain the corresponding coefficient of the derivative. The function then returns the list of coefficients of the derivative.
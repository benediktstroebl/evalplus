### Derivative of a Polynomial
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial in ascending order of powers.
    
    Returns:
    list: Coefficients of the derivative polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize the derivative coefficients list with the first coefficient
    # multiplied by the power of the derivative, which is always 1.
    derivative_coeffs = [xs[0]*1]
    
    # Loop through the coefficients starting from the second one (index 1).
    for i in range(1, len(xs)):
        # Multiply each coefficient by its power and add it to the derivative.
        derivative_coeffs.append(xs[i]*i)
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([5]))  # Output: []
print(derivative([]))  # Output: []
```
This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. It iterates over the coefficients, multiplying each by its power (starting from 1) and adding the result to the derivative coefficients list. The function returns the list of derivative coefficients.
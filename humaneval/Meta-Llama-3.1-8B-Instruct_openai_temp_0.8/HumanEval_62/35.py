```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): List of coefficients of the polynomial.
               xs[i] is the coefficient of x^i.

    Returns:
    list: List of coefficients of the derivative polynomial.
    """
    # Initialize an empty list to store the derivative coefficients
    derivative_coeffs = [0] * (len(xs) - 1)
    
    # Calculate the derivative coefficients
    for i in range(1, len(xs)):
        derivative_coeffs[i - 1] = i * xs[i]
    
    return derivative_coeffs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script defines a function `derivative` that calculates the coefficients of the derivative of a polynomial represented as a list of coefficients. The function iterates over the list, starting from the second element (index 1), and multiplies each element by its index minus 1 (to get the derivative coefficient). The result is a new list with the derivative coefficients, which is then returned. The script also includes test cases to demonstrate the function's correctness.
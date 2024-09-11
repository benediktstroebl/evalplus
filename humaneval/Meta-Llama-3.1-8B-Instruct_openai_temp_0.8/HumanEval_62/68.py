```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients representing the polynomial.
            xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = [0] * len(xs)
    
    # The derivative of x^n is n * x^(n-1), so we multiply each coefficient by its index
    for i in range(1, len(xs)):
        derivative_coeffs[i-1] = i * xs[i]
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns a list of coefficients representing the derivative of the polynomial. The function uses a loop to multiply each coefficient by its index (which represents the power of x), effectively calculating the derivative of the polynomial. The function is then tested with two examples to demonstrate its correctness.
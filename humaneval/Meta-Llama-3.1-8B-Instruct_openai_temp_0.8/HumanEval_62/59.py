```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial.
    The polynomial is represented as a list of coefficients, where the first coefficient is the constant term,
    the second coefficient is the coefficient of x, the third coefficient is the coefficient of x^2, and so on.

    Args:
        xs (list): A list of coefficients representing a polynomial.

    Returns:
        list: A list of coefficients representing the derivative of the input polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []
    
    # If the polynomial has degree 0 (i.e., it's a constant), its derivative is 0
    if len(xs) == 1:
        return derivative_coeffs
    
    # If the polynomial has degree 1 (i.e., it's a linear polynomial), its derivative is the coefficient of x
    if len(xs) == 2:
        return derivative_coeffs + [xs[1]]
    
    # For polynomials of degree 2 or more, the derivative is calculated by multiplying each coefficient by its degree
    # and subtracting the product of the next coefficient and its degree minus one
    for i in range(1, len(xs) - 1):
        derivative_coeffs.append(xs[i] * i)
    
    derivative_coeffs.append(xs[-1] * (len(xs) - 1))
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a list of coefficients representing the derivative of the input polynomial. It uses list comprehension and basic arithmetic operations to calculate the derivative. The function also includes docstrings and example use cases to illustrate its usage.
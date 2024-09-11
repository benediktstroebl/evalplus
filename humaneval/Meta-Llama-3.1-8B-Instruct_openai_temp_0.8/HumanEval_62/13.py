```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a given polynomial.
    
    The polynomial is represented as a list of coefficients, where each coefficient
    corresponds to a power of x. The derivative is calculated by applying the power
    rule of differentiation, which states that the derivative of x^n is nx^(n-1).
    
    Args:
    xs (list): A list of coefficients representing the polynomial.
    
    Returns:
    list: A list of coefficients representing the derivative of the polynomial.
    """
    
    # Initialize an empty list to store the coefficients of the derivative
    derivative_xs = [0] * (len(xs) - 1)
    
    # Calculate the derivative of each term in the polynomial
    for i in range(1, len(xs)):
        # The coefficient of the derivative of x^n is n times the coefficient of x^n
        derivative_xs[i - 1] = i * xs[i]
    
    return derivative_xs

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This Python function works by iterating over the coefficients of the input polynomial, starting from the second coefficient (since the first coefficient is the constant term, which has a derivative of 0). For each coefficient, it calculates the derivative by multiplying the coefficient by its power (which is its index in the list). The resulting coefficients are stored in a new list, which is returned as the derivative of the polynomial.
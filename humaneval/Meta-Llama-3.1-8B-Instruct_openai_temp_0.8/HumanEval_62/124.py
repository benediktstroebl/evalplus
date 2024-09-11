```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    The input is a list of coefficients, where xs[i] is the coefficient of x^i.
    
    The output is a list of coefficients of the derivative, where the coefficients are
    the derivative of the original polynomial's coefficients.
    
    For example, if the original polynomial is 3 + 1x + 2x^2 + 4x^3 + 5x^4,
    then the derivative is 1 + 4x + 12x^2 + 20x^3.
    
    :param xs: A list of coefficients of a polynomial.
    :return: A list of coefficients of the derivative of the polynomial.
    """
    # The derivative of a constant is 0
    if not xs:
        return []
    
    # The derivative of x^i is i*x^(i-1)
    # So, the derivative of xs[i] * x^i is i*x^(i-1) * xs[i]
    # We use a list comprehension to calculate the new coefficients
    return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([0, 1]))  # [1]
print(derivative([]))  # []
```

This script defines a function `derivative` that takes a list of coefficients as input and returns a list of coefficients of the derivative of the polynomial. The function uses list comprehension to calculate the new coefficients. The test cases at the end of the script demonstrate the function's behavior.
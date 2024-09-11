### Derivative of a Polynomial
#### Problem Description
Given the coefficients of a polynomial in the form `xs[0] + xs[1] * x + xs[2] * x^2 +...`, compute the derivative of the polynomial.

#### Solution
```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients representing the polynomial.
              xs[i] is the coefficient of x^i.

    Returns:
    list: A list of coefficients representing the derivative of the polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative
    derivative_coeffs = []
    
    # The derivative of xs[0] is 0, so we start from the first non-zero coefficient
    for i in range(1, len(xs)):
        # The derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2)
        # So, the coefficient of the derivative is i * xs[i]
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients as input and returns a list of coefficients representing the derivative of the polynomial. The function iterates over the input list starting from the first non-zero coefficient and computes the coefficients of the derivative using the power rule of differentiation.
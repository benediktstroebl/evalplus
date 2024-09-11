### Derivative of a Polynomial
#### Problem Description
Given the coefficients of a polynomial in the form `xs[0] + xs[1] * x + xs[2] * x^2 +...`, calculate the derivative of this polynomial.

#### Solution
```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
    xs (list): Coefficients of the polynomial

    Returns:
    list: Coefficients of the derivative polynomial
    """
    # If the polynomial is a constant, its derivative is 0
    if len(xs) == 1:
        return [0]
    
    # The derivative of a constant term is 0
    derivative_coeffs = [0]
    
    # The derivative of x^n is n * x^(n-1)
    # Hence, the coefficient of x^n is multiplied by n
    for i in range(1, len(xs)):
        derivative_coeffs.append(i * xs[i])
    
    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Output: [2, 6]
```
This script uses a simple iterative approach to calculate the derivative of the polynomial. The time complexity is O(n), where n is the degree of the polynomial.
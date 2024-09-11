### Derivative of a Polynomial
#### Overview
This Python script calculates the derivative of a polynomial given its coefficients.

#### Code

```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): List of coefficients of the polynomial.

    Returns:
        list: List of coefficients of the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Use list comprehension to calculate the derivative coefficients
    # The power of each term in the derivative is one less than the original term
    # For example, the derivative of x^n is n*x^(n-1)
    # So, the derivative coefficients are obtained by multiplying the original coefficients
    # by their corresponding powers and then subtracting one from the power
    derivative_coeffs = [(i * x) for i, x in enumerate(xs[1:], 1)]
    
    return derivative_coeffs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

#### Explanation
This script defines a function `derivative(xs)` that calculates the derivative of a polynomial given its coefficients. It uses list comprehension to iterate over the coefficients, multiplying each one by its corresponding power (i.e., its index) and subtracting one from the power. The result is a new list of coefficients representing the derivative polynomial. The example usage at the end demonstrates how to use this function to calculate the derivatives of two sample polynomials.
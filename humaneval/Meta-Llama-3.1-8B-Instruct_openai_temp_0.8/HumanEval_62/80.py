### Calculating the Derivative of a Polynomial
#### A Python Script
```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Parameters:
    xs (list): A list of coefficients of the polynomial, where xs[0] is the constant term,
               xs[1] is the coefficient of the linear term, and so on.
    
    Returns:
    list: A list of coefficients of the derivative polynomial.
    
    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_xs = [i * coeffs for i, coeffs in enumerate(xs[1:], 1)]
    return derivative_xs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script uses list comprehension to efficiently calculate the derivative of the polynomial. It iterates over the coefficients of the polynomial (excluding the constant term), multiplying each by its index (representing the power of x) and storing the results in a new list. The function then returns this list, which represents the coefficients of the derivative polynomial.
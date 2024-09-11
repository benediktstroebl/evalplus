### Polynomial Derivative Calculator
#### Python Script
```markdown
### Description
This script calculates the derivative of a polynomial given its coefficients.

### Code
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial, where xs[0] is the constant term,
               xs[1] is the coefficient of x, and so on.

    Returns:
    list: Coefficients of the derivative polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to store the coefficients of the derivative polynomial
    derivative_coeffs = []

    # Iterate over the coefficients of the original polynomial, starting from the second coefficient
    for i in range(1, len(xs)):
        # For each coefficient, multiply it by its index and append it to the derivative polynomial
        derivative_coeffs.append(i * xs[i])

    # Return the coefficients of the derivative polynomial
    return derivative_coeffs
```

### Example Use Cases
```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

### Explanation
This script works by iterating over the coefficients of the original polynomial, starting from the second coefficient (index 1). For each coefficient, it multiplies it by its index and appends the result to the derivative polynomial. The result is a new list of coefficients that represent the derivative polynomial. Note that the index of each coefficient in the derivative polynomial is one less than its index in the original polynomial.
```python
# Original polynomial: 3 + 1x + 2x^2 + 4x^3 + 5x^4
# Derivative polynomial: 0 + 1x + 2*2x^1 + 3*3x^2 + 4*4x^3

# Original coefficients: [3, 1, 2, 4, 5]
# Derivative coefficients: [0, 1, 6, 12, 16] -> [1, 4, 12, 20] after removing the first element
```
### Derivative of a Polynomial
#### Python Script
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial.

    Args:
    xs (list): Coefficients of the polynomial, where xs[0] is the constant term,
               xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, etc.

    Returns:
    list: Coefficients of the derivative polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Check if the input list is empty
    if not xs:
        raise ValueError("Input list cannot be empty")

    # Initialize the derivative coefficients list
    deriv = []

    # Calculate the derivative coefficients
    # For each power of x in the original polynomial, the corresponding power in the derivative polynomial is x^(power-1)
    # The coefficient of x^(power-1) in the derivative polynomial is power times the coefficient of x^power in the original polynomial
    for power in range(1, len(xs)):
        # Multiply the coefficient of x^power by power
        deriv.append(power * xs[power])

    return deriv

# Test the derivative function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
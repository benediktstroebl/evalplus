### Derivative of a Polynomial
#### Self-Contained Python Script

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

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
    # Handle the edge case where the polynomial is a constant (one coefficient)
    if len(xs) == 1:
        return []
    
    # Initialize the list to store coefficients of the derivative
    derivative_xs = []

    # Iterate over the coefficients of the polynomial
    for i in range(1, len(xs)):
        # For each coefficient, multiply it by its power (i) and add it to the derivative
        derivative_xs.append(i * xs[i])

    return derivative_xs

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

This script defines a function `derivative(xs)` that calculates the derivative of a polynomial represented by the list of coefficients `xs`. The function handles the edge case where the polynomial is a constant and returns an empty list. The derivative of the polynomial is calculated by multiplying each coefficient by its power (i) and adding it to the list of coefficients of the derivative. The function is then tested with two examples.
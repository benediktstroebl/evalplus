### Derivative of a Polynomial
#### Python Implementation

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial. xs[i] represents the coefficient of x^i.

    Returns:
        list: Coefficients of the derivative polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Initialize derivative coefficients with None
    dxs = [None] * (len(xs) - 1)

    # Calculate derivative coefficients
    for i in range(len(xs) - 1):
        # Derivative of x^i is i * x^(i-1)
        dxs[i] = i * xs[i + 1]

    return dxs

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

In this script, we define a function `derivative` that takes a list of polynomial coefficients `xs` and returns the coefficients of the derivative polynomial. The function iterates over the input coefficients, applying the power rule of differentiation (i.e., derivative of x^i is i * x^(i-1)) to each term. The resulting derivative coefficients are returned as a new list.
```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial represented by coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +....

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # If the polynomial is a constant (only one non-zero coefficient), the derivative is 0.
    if len(xs) == 1:
        return [0]
    
    # The derivative of a polynomial is calculated by multiplying each coefficient by its index and shifting it one position to the left.
    # This is equivalent to the mathematical formula: d(xs[i] * x^i)/dx = i * xs[i] * x^(i-1)
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
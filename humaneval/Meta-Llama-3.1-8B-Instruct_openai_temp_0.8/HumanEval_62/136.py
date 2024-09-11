```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): List of coefficients of a polynomial.

    Returns:
        list: List of coefficients of the derivative of the polynomial.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # If the polynomial is of degree 0, its derivative is 0.
    if len(xs) == 1:
        return [0]
    
    # Derivative of x^n is n * x^(n-1)
    # Therefore, the derivative of the polynomial is the list of coefficients
    # shifted one position to the left and multiplied by their original positions.
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Expected output: [2, 6]
```

This script defines a function `derivative(xs: list)` that takes a list of coefficients `xs` of a polynomial and returns the list of coefficients of the derivative of the polynomial. The function uses a list comprehension to calculate the derivative of each term in the polynomial. It shifts the list of coefficients one position to the left and multiplies each coefficient by its original position, starting from 1. The function also includes test cases at the end to verify its correctness.
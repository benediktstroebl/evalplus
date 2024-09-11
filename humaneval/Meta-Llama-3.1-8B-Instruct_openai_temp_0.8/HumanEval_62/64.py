```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` of a polynomial and returns a new list representing the coefficients of the polynomial's derivative. The derivative is calculated using the formula `d(x^n)/dx = n*x^(n-1)`. The function uses a list comprehension to generate the new list of coefficients.

The script also includes two test cases to verify the function's correctness.
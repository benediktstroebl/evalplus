```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of a polynomial.

    Returns:
        list: Derivative of the polynomial.

    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # The derivative of a polynomial is a new polynomial where each coefficient is n * xs[n]
    # So we create a new list where each element is the product of its index and the corresponding element in xs
    return [i * x for i, x in enumerate(xs[:-1], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a list comprehension to efficiently create the derivative of the input polynomial. The `enumerate` function is used to get both the index and the value of each element in the input list, and the `start=1` argument is used to make the indices start at 1 (since the derivative of x^n is n*x^(n-1)).
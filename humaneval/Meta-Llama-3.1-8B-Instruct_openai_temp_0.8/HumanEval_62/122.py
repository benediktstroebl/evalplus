```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial.

    The input list represents coefficients of a polynomial in descending order of powers.
    The output list contains coefficients of the derived polynomial.

    Args:
        xs (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derived polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # Shift coefficients to the right by one position (ignoring the constant term)
    # This is equivalent to differentiating each term by one power of x
    return [i * x for i, x in enumerate(xs[1:], 1)]


# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This Python function takes a list of coefficients representing a polynomial and returns the derivative of that polynomial in the same form. The function uses list comprehension to shift the coefficients to the right by one position, effectively differentiating each term by one power of x. The `enumerate` function is used to pair each coefficient with its new index (which starts from 1 for the first non-constant term), and the list comprehension uses this pair to calculate the new coefficient.
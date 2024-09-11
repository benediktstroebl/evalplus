```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients representing the polynomial.
            The i-th element of the list represents the coefficient of the i-th degree term.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    # We shift the indices of the coefficients down by one, and multiply each one by its current index
    # Since the derivative of x^n is n*x^(n-1), we multiply by the current index (which is the degree of the term)
    # and then shift all the indices down, since the derivative of a term of degree n is a term of degree n-1
    return [i * xs[i] for i in range(1, len(xs))]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script uses a list comprehension to calculate the derivative of the polynomial. It multiplies each coefficient by its index (which represents the degree of the term) and then shifts all the indices down by one. The result is a new list of coefficients representing the derivative of the polynomial.
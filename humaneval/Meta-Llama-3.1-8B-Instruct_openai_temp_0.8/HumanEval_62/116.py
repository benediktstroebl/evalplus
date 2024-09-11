```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial given its coefficients.

    The polynomial is assumed to be in the form:
    xs[0] + xs[1] * x + xs[2] * x^2 +...

    Args:
        xs (list): A list of coefficients of the polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient
    # by its index (except the first one, which is 0) and remove the first element.
    return [i * x for i, x in enumerate(xs[1:], 1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([0, 0]))  # Expected output: []
```

This script uses list comprehension and the `enumerate` function to efficiently compute the derivative of the polynomial. The `enumerate` function returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over the sequence. We use this to get the index of each element in the list, multiply it by the element, and create a new list. The `enumerate` function is used with the `start` argument set to 1 to get the indices starting from 1, which corresponds to the exponent of the polynomial. The `[1:]` slice is used to exclude the first element (at index 0) from the calculation.
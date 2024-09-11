```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of a polynomial.
                  xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    # The derivative of x^n is n*x^(n-1)
    # So we multiply each coefficient by its index and shift the list to the left
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script uses list comprehension to create the derivative of the polynomial. It iterates over the list of coefficients (excluding the first one, which is the constant term), multiplying each coefficient by its index (which is equivalent to its degree) and storing the results in a new list. The `enumerate` function is used to get both the index and the value of each element in the list, and the `1:` argument is used to start the enumeration from the second element (index 1).
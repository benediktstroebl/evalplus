```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): A list of coefficients representing a polynomial.
                   The coefficient at index i represents the coefficient of x^i.

    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
    """
    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its index and shift the array
    return [i * x for i, x in enumerate(xs[1:], start=1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Expected output: [2, 6]
```

In this script, the `derivative` function uses a list comprehension to calculate the derivative of the polynomial. It iterates over the coefficients, shifting the index by 1 to account for the fact that the derivative of x^n is n*x^(n-1). The `enumerate` function is used to get both the index and the value of each item in the list, and the `start=1` argument is used to start the index from 1 instead of 0.
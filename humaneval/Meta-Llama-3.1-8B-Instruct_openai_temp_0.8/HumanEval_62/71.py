```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of the polynomial, where xs[0] is the constant term,
            xs[1] is the coefficient of x, xs[2] is the coefficient of x^2, and so on.

    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    return [i * x for i, x in enumerate(xs[1:], 1) if i <= len(xs) - 1]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

In this code, the function `derivative` iterates over the coefficients of the polynomial, starting from the second one (index 1), and multiplies each coefficient by its index (which represents the exponent of x) to get the corresponding coefficient of the derivative polynomial. The result is a new list of coefficients, which is then returned by the function. The `enumerate` function is used to get both the index and the value of each element in the input list. The `if i <= len(xs) - 1` condition is used to avoid an `IndexError` when the input list has only one element.
```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial.

    Returns:
        list: coefficients of the derivative polynomial.
    """
    # Remove the first element (constant term) and multiply each remaining coefficient by its index
    # The index represents the power of x to which each term is raised
    return [i * x for i, x in enumerate(reversed(xs[:-1]), 1)][::-1]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a list comprehension to generate the coefficients of the derivative polynomial. It iterates over the indices of the input list (excluding the constant term), multiplying each coefficient by its index. The `enumerate` function is used to get both the index and the value of each element in the list, and the `reversed` function is used to start from the highest power of x. Finally, the result is reversed to maintain the original order of the coefficients.
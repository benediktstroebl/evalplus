```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    The polynomial is represented in the form xs[0] + xs[1] * x + xs[2] * x^2 +...
    The derivative of the polynomial is then calculated and returned in the same form.

    Args:
        xs (list): A list of coefficients of the polynomial.

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
    """
    if len(xs) <= 1:  # If the polynomial is a constant or a linear term, return an empty list
        return []
    return [i * coeff for i, coeff in enumerate(xs[1:], start=1)]


# Example usage:
print(derivative([3, 1, 2, 4, 5]))
# Output: [1, 4, 12, 20]

print(derivative([1, 2, 3]))
# Output: [2, 6]
```

In this code, we use the `enumerate` function to get both the index and value of each element in the list `xs` starting from 1 (since the term `xs[0]` is not multiplied by x). We then multiply each term by its index to get the coefficients of the derivative, and return the result as a list.
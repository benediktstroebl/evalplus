```python
def derivative(xs: list):
    """
    Derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of a polynomial in descending order of powers.

    Returns:
    list: Coefficients of the polynomial's derivative.
    """
    if len(xs) == 1:  # base case: derivative of constant is 0
        return []

    return [i * coefficient for i, coefficient in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

In this script, we use a list comprehension to generate the coefficients of the polynomial's derivative. The `enumerate` function is used to iterate over both the index and the value of each element in the `xs` list, starting from the second element (index 1). The `start=1` argument ensures that we multiply each coefficient by its index (i.e., the power of x it corresponds to). If the input list has only one element, we return an empty list, as the derivative of a constant is 0.
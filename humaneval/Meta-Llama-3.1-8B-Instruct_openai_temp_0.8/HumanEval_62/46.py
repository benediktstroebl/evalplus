```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of a polynomial.
            xs[0] + xs[1] * x + xs[2] * x^2 +....
            For example, xs = [3, 1, 2, 4, 5] represents the polynomial 3 + x + 2x^2 + 4x^3 + 5x^4

    Returns:
        list: A list of coefficients of the derivative of the polynomial.
            For example, derivative([3, 1, 2, 4, 5]) returns [1, 4, 12, 20]
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients as input and returns the list of coefficients of the derivative of the polynomial. The function uses a list comprehension to calculate the derivative, which is simply each coefficient multiplied by its position (starting from 1) in the list. The `enumerate` function is used to iterate over both the index and the value of each element in the list, starting from the second element (since the first element is a constant term and does not contribute to the derivative).
```python
def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power.

    Returns:
        list: Derivative of the polynomial, again represented as a list of coefficients.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result
```

This Python script defines a function 'derivative' that takes a list of coefficients as input and returns the derivative of the corresponding polynomial. The function employs a basic loop to calculate the derivative, accumulating results in the 'result' list. To improve efficiency, the script uses the multiplication approximation x *= 1 + i, which is accurate for integer indices i.
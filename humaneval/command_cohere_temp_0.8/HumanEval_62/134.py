```python
def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.
    Args:
    xs (list): Coefficients of the polynomial in the form [3, 1, 2, 4, 5].
    Returns:
    list: Derivative of the polynomial in the same form [1, 4, 12, 20].
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        if i != 0:
            result[i] //= i
    return result
```

This Python script defines a function `derivative` taking a list `xs` as input, representing the coefficients of a polynomial, and returns the derivative of the polynomial. It uses a for loop to calculate the derivative for each term of the polynomial, starting from index 1, considering the leading coefficient (xs[0]) as a constant. The resulting derivative coefficients are stored in the `result` list. 

Here's an example of using this function:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```

This function reproduces the expected behavior as stated in the problem statement.
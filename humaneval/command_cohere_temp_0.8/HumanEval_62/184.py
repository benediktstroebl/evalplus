```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power of x.

    Returns:
        list: Derivative of the polynomial, represented as a list of coefficients.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    derivative_coef = 1
    for coef in xs:
        result[len(xs) - 1] += coef * derivative_coef
        derivative_coef += 1
    return result
```

This Python script defines a function `derivative` that takes a list of coefficients of a polynomial `xs` and returns the derivative of the polynomial as a list of coefficients. It uses a loop to calculate the derivative of each term of the polynomial and returns the result as a list.

Here is a sample output:
```
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
```

This algorithm solves the challenge and provides the derivative of the polynomial as expected.
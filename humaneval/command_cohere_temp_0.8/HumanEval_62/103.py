```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power of x.

    Returns:
        list: Derivative of the polynomial, represented in the same format.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        x += 1
    return result
```

The derivative of a polynomial is given by:
```
(ax^n) => (anx^(n-1))
```

The derivative operator acts on each term of the polynomial according to this rule. Our function compiles these individual derivatives into a list to return the result.
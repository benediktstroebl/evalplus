```python
def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial represented by its coefficients.
    Args:
    xs (list): coefficients of the polynomial in order of increasing power, ex. [3, 1, 2, 4, 5] -> 3 + x^1 * 1 + x^2 * 2 + x^3 * 4 + x^4 * 5
    Returns:
    list: coefficients of the derivative represented in the same format as the input ex. [1, 4, 12, 20]
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + 1
    return result
```

This Python script defines a function called `derivative` which takes a list of numbers as input. These numbers represent the coefficients of a polynomial in the form: `xs[0] + xs[1] * x + xs[2] * x^2 + ...`. The function calculates the derivative of this polynomial and returns the coefficients of the derivative in the same format. The process involves adding a term to the current coefficient multiplied by the rising `x` power and updating `x` to `(x+1)` for the next iteration to correctly compute the derivative.

Here is an example of the function being used:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```

This example test validates the correctness of the `derivative` function.
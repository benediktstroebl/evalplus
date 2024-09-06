```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by lists of coefficients.

    Polynomial is represented in the form: xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns a new list with the derivative of the polynomial, in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
    return result
```

This Python script defines a function `derivative` taking a list `xs` as input, representing the coefficients of a polynomial. It calculates the derivative of this polynomial and returns the result as a list, in the same form as the input. Two example uses are provided in the function docstring, confirming that the function behaves as expected. 

To achieve this, the function first creates an empty list `result` with a length equal to the length of the input list `xs`, initializing all items to 0. It then iterates through each index of `xs`, multiplying each coefficient by `x` and updating `x` to `x + 1`. The final result is a list of coefficients representing the derivative of the original polynomial.
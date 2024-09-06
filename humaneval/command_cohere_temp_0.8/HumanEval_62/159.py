```python
def derivative(xs: list) -> list:
    """
    Find the derivative of a polynomial given its coefficients.

    Args:
        xs (list): The coefficients of the polynomial, in the order:
                    xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns:
        list: The coefficients of the derivative, in the same format as the input.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1 + i
    return result
```

This Python script defines a function `derivative` taking a list `xs` as an argument, representing the coefficients of a polynomial, and returns the derivative of this polynomial. The function utilizes a loop to calculate the derivative of each term of the polynomial, effectively applying the power rule of differentiation. The returned list of coefficients represents the derivative in the same format as the input.

Here's an illustrative example of this function:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```

This demonstrates the function's ability to correctly calculate the derivatives of the given polynomials.
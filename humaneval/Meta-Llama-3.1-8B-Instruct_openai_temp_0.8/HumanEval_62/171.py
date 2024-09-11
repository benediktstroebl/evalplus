### Derivative of a Polynomial
#### Solution

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] is the constant term, xs[1] is the coefficient of x, etc.

    Returns:
    list: A list of coefficients of the derivative of the polynomial.

    Example:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of x^n is n*x^(n-1)
    # We start from the second coefficient (index 1) because the derivative of x^n is n*x^(n-1)
    # The first coefficient (index 0) in the result is the derivative of the constant term, which is 0
    return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This Python script defines a function `derivative(xs)` that calculates the derivative of a polynomial given its coefficients. It uses a list comprehension to create a new list of coefficients, where each coefficient is the product of its index (i) and the corresponding coefficient from the input list. The function then returns this new list.

The script includes a docstring that explains the purpose of the function, its input and output parameters, and provides example usage.
```python
def derivative(xs: list) -> list:
    """
    Returns the derivative of a polynomial given its coefficients.

    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]

    :param xs: coefficients of the polynomial
    :return: coefficients of the derivative
    """
    if len(xs) == 0:  # base case: derivative of a constant is 0
        return []
    return [i * xs[i] for i in range(1, len(xs))]  # return derivative coefficients

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([]))  # Output: []
```

This script defines a function `derivative` that takes a list of coefficients `xs` as input and returns the coefficients of the derivative of the polynomial represented by `xs`. The function uses list comprehension to calculate the derivative coefficients. The test cases at the end demonstrate the function's behavior with different inputs.
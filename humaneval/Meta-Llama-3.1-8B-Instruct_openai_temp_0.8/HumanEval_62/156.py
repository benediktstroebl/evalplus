### Derivative of a Polynomial
#### A Python Function to Calculate the Derivative of a Polynomial

```python
def derivative(xs: list) -> list:
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): A list of coefficients of a polynomial.
               xs[0] + xs[1] * x + xs[2] * x^2 +...

    Returns:
    list: The derivative of the polynomial in the same form.
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example use cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

In this script, the function `derivative` takes a list of coefficients `xs` and returns the derivative of the corresponding polynomial. The derivative is calculated by multiplying each coefficient (except the first one) by its index, which is the power of x that coefficient corresponds to.
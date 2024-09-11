```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial.

    Returns:
        list: coefficients of the derivative polynomial.
    """
    return [i * coefficient for i, coefficient in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))
# [1, 4, 12, 20]
print(derivative([1, 2, 3]))
# [2, 6]
```

This script defines a function `derivative` that takes a list of coefficients `xs` as input and returns the coefficients of the derivative polynomial. It uses a list comprehension to iterate over the input list, multiplying each coefficient by its index (starting from 1) to compute the corresponding coefficient in the derivative polynomial. The `enumerate` function is used to generate the indices and corresponding values from the input list. The `start=1` argument to `enumerate` is used to start the index from 1 instead of the default 0.
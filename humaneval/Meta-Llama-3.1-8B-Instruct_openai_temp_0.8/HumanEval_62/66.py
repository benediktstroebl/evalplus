```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        # Special case for constant polynomial
        return []
    else:
        # Derivative of xs[i] * x^(i-1) is i * xs[i] * x^(i-2)
        # So we multiply each coefficient by its index and remove the first element
        return [i * x for i, x in enumerate(xs[1:], 1)]


# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1]))  # []
print(derivative([]))  # []
```

In this script, we define a function `derivative` that takes a list of coefficients `xs` as input. We first handle the special case where the input list has only one element (i.e., the constant polynomial). Otherwise, we use a list comprehension to calculate the derivative of the polynomial. The derivative of `xs[i] * x^(i-1)` is `i * xs[i] * x^(i-2)`, so we multiply each coefficient `x` by its index `i` and remove the first element of the list. We then print the results of some test cases to verify that the function works correctly.
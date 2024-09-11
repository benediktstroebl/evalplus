```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a polynomial ax^n is nax^(n-1)
    # So, the corresponding coefficient is n times the original coefficient
    # We start from the second coefficient (index 1) and multiply it by its index (starting from 1)
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

In this script, we use list comprehension to create a new list where each element is the product of its index (starting from 1) and the corresponding element in the original list, but starting from the second element (index 1). This corresponds to the formula for the derivative of a polynomial.
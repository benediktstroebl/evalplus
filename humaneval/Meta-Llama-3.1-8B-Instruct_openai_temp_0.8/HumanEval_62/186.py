```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.

    :param xs: list of coefficients of the polynomial
    :return: list of coefficients of the derivative
    """
    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its index
    # and shift the resulting list to the right (by slicing).
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

This script works by using list comprehension to create a new list where each element is the product of its index and the corresponding element in the input list. The `enumerate` function is used to get both the index and the value of each element in the list, and the `start=1` argument is used to make the index start at 1 (since the first element of the polynomial corresponds to x^0, not x^1).
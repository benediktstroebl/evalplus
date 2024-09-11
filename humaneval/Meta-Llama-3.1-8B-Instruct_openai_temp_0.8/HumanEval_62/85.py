```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): Coefficients of a polynomial.

    Returns:
        list: Coefficients of the derivative of the polynomial.
    """
    # The derivative of a polynomial xs[0] + xs[1] * x +... + xs[n] * x^n is
    # xs[1] + 2xs[2] * x +... + nxs[n] * x^(n-1)
    # Therefore, we start from the second coefficient (index 1) and multiply
    # each coefficient by its index (which is the power of x it's multiplied by)
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script defines a function `derivative` that calculates the derivative of a polynomial given its coefficients. The function uses a list comprehension to create a new list where each coefficient is multiplied by its index (which represents its power of x). The script then tests the function with two examples from the problem statement.
```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.

    Args:
        xs (list): coefficients of the polynomial

    Returns:
        list: coefficients of the derivative polynomial
    """
    if len(xs) == 0:
        return []
    elif len(xs) == 1:
        return []
    else:
        # derivative of a*x^n is n*a*x^(n-1)
        # so we multiply each coefficient by its index and subtract one from the index
        return [i * x for i, x in enumerate(xs[1:], 1)]

# test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([0, 1, 2]))  # [1, 4]
print(derivative([4]))  # []
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns a new list of coefficients representing the derivative of that polynomial. The function uses a list comprehension to multiply each coefficient by its index and subtract one from the index, then returns the resulting list of coefficients. If the input list is empty or has only one element, the function returns an empty list, since the derivative of a constant is zero and the derivative of a polynomial of degree zero is zero.
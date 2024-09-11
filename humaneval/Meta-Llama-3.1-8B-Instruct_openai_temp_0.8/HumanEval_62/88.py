### Calculating Derivative of a Polynomial
#### Code
```python
def derivative(xs: list):
    """
    Calculate the derivative of a polynomial given its coefficients.

    Args:
    xs (list): Coefficients of the polynomial (from lowest to highest degree).

    Returns:
    list: Coefficients of the derivative polynomial (from lowest to highest degree).
    """
    # Shift coefficients one position to the left (divide by power + 1)
    # and drop the first coefficient (constant term)
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example use cases:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([0]))  # []
print(derivative([]))  # []
```

#### Explanation

The script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns a list of coefficients of the derivative polynomial.

The function uses list comprehension to create the derivative coefficients. It shifts the coefficients one position to the left by multiplying each coefficient by its position (starting from 1) and dropping the first coefficient (which is the constant term).
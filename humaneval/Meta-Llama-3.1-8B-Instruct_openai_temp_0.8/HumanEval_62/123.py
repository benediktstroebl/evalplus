```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:  # Base case: polynomial is constant
        return []
    
    # Remove the first coefficient (constant term) and multiply each remaining coefficient by its index
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
print(derivative([1]))  # []
print(derivative([]))  # []
```

This script defines a function `derivative` that takes a list of coefficients representing a polynomial and returns the coefficients of its derivative. The function uses a list comprehension to generate the derivative coefficients, iterating over the list of coefficients (excluding the constant term) and multiplying each coefficient by its index (starting from 1). The test cases demonstrate the function's correctness.
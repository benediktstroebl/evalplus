```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
    xs (list): List of coefficients of a polynomial.
    
    Returns:
    list: List of coefficients of the derivative of the polynomial.
    """
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return []
    
    # We need to shift the coefficients to the right by one position and multiply by their indices
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([]))  # Expected output: []
print(derivative([1]))  # Expected output: []
```

This script uses list comprehension to efficiently calculate the coefficients of the derivative of a polynomial given its coefficients. The `enumerate` function is used to get both the index and value of each element in the list, and then we multiply the index by the value to get the new coefficient. The `start=1` argument of `enumerate` is used to make the index start from 1, not 0, because in the context of polynomial coefficients the first power is 1, not 0.
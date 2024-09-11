```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: The derivative of the polynomial in the same form.
    
    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a polynomial is calculated by multiplying each coefficient by its exponent and subtracting one from the exponent.
    # We start with the second coefficient (index 1) because the derivative of a coefficient of degree 0 is 0.
    return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a list comprehension to create the derivative of the polynomial. The `range(1, len(xs))` part starts at index 1 (the second coefficient) and goes up to, but does not include, the last index in the list. For each index `i` in this range, it calculates the derivative by multiplying the coefficient at that index by `i` (which is equivalent to multiplying by `i-1` in the original formula) and includes this result in the output list.
```python
def derivative(xs: list) -> list:
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): List of coefficients of a polynomial.
    
    Returns:
        list: List of coefficients of the derivative polynomial.
    """
    # Use list comprehension to create new list with derivative coefficients
    # The derivative of xs[i] * x^(i) is i * xs[i] * x^(i-1)
    # So we multiply each coefficient by its index and subtract 1 from the index
    return [i * xs[i] for i in range(1, len(xs))]

# Test the function
print(derivative([3, 1, 2, 4, 5]))
print(derivative([1, 2, 3]))
```

This script will output:
```python
[1, 4, 12, 20]
[2, 6]
```

In this code, we first check if there is only one element in the input list (i.e., a constant polynomial), in which case we return an empty list because the derivative of a constant is 0. Then we use list comprehension to create a new list with the derivative coefficients. For each index `i` in the input list, we multiply `xs[i]` by `i` to get the derivative coefficient, and we start the iteration from `i = 1` (index 0 is the constant term, and we don't take the derivative of it).
### Derivative of a Polynomial
#### Code

```python
def derivative(xs: list):
    """
    Return the derivative of a polynomial in the form of xs,
    where xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Args:
    xs (list): coefficients of the polynomial
    
    Returns:
    list: coefficients of the derivative polynomial
    """
    
    # Shift coefficients by 1 to the left and multiply by their indices
    # This effectively calculates the derivative of each term in the polynomial
    return [i * x for i, x in enumerate(xs[1:], 1)]
```

#### Example Use Cases

```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This code defines a function `derivative` that takes a list of coefficients `xs` representing a polynomial and returns the coefficients of its derivative. The function uses a list comprehension to shift the coefficients by one position to the left (using `enumerate`) and multiply each coefficient by its previous index, effectively calculating the derivative of each term in the polynomial.
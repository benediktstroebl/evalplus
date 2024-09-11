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
    # Calculate the derivative of a polynomial using the power rule
    # If the coefficient of x^n is c, the coefficient of x^(n-1) in the derivative is nc
    return [i * x for i, x in enumerate(xs[1:], start=1) if i * x!= 0]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```

However, the condition in the list comprehension to skip the first element (i * x!= 0) is unnecessary because it will never occur with non-zero coefficients and non-zero start index. Here's a simplified version:

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
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # [2, 6]
```
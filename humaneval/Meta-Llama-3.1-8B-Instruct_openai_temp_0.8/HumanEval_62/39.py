### Derivative of a Polynomial
#### Python Script

```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of a polynomial. 
               xs[0] is the constant term, xs[1] is the coefficient of x, xs[2] is the coefficient of x^2 and so on.
    
    Returns:
    list: A list of coefficients of the derivative of the polynomial.
    """
    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its index,
    # and then remove the first element (the coefficient of x^0) because it's 0.
    return [i * x for i, x in enumerate(xs[1:], 1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses a list comprehension to efficiently calculate the derivative of the polynomial. The `enumerate` function is used to get both the index and the value of each element in the list, starting from 1 (because the coefficient of x^0 is 0).
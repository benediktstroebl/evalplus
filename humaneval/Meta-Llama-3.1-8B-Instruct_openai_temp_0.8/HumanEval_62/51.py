```python
def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    
    Args:
        xs (list): A list of coefficients of the polynomial.
        
    Returns:
        list: A list of coefficients of the derivative polynomial.
    """
    # Remove the first element as it is the constant term and its derivative is 0
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
print(derivative([4]))  # Output: []
print(derivative([]))  # Output: []
```

This script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns a new list representing the coefficients of the derivative of the polynomial. The derivative of a polynomial is calculated by differentiating each term with respect to x and multiplying the coefficient of each term by the power of x. In this case, the function uses a list comprehension to generate the coefficients of the derivative polynomial. The `enumerate` function is used to get both the index and the value of each element in the list, and the `start` parameter is used to start the index from 1 instead of 0.
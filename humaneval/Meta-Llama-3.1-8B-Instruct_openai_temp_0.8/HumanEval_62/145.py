```python
def derivative(xs: list) -> list:
    """
    This function calculates the derivative of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of a polynomial.
              xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
    list: The coefficients of the derivative of the polynomial.
          derivative(xs[0]) + derivative(xs[1]) * x + derivative(xs[2]) * x^2 +....
    """
    return [i * x for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
print(derivative([1]))  # Expected output: []
print(derivative([]))  # Expected output: []
```

In this script, the `derivative` function uses a list comprehension to calculate the derivative of a polynomial given its coefficients. It iterates over the coefficients starting from the second one (since the first one is the constant term, which has a derivative of 0), multiplies each coefficient by its position (which is equivalent to multiplying by its power of x), and returns the resulting list of coefficients. The test cases demonstrate the function's usage and expected outputs.
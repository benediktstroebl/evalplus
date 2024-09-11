```python
def derivative(xs: list):
    """
    This function calculates the derivative of a polynomial given its coefficients.

    Args:
        xs (list): A list of coefficients of a polynomial. 
            xs[0] + xs[1] * x + xs[2] * x^2 +....
    
    Returns:
        list: The coefficients of the derivative polynomial.
    """
    # Remove the leading coefficient (if exists) since it's not multiplied by x
    return [x * i for i, x in enumerate(xs[1:], start=1)]

# Test cases
print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Expected output: [2, 6]
```

This script uses a list comprehension to generate the derivative coefficients. It starts from the second coefficient (index 1) and multiplies each coefficient by its corresponding power (1, 2, 3,...). The `enumerate` function is used to get both the index and the value of each item in the list. The `start=1` argument tells `enumerate` to start counting from 1 instead of 0.
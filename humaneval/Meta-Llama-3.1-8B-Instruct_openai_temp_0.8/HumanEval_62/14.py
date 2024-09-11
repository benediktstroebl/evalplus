```python
def derivative(xs: list) -> list:
    """
    This function takes a list of coefficients of a polynomial as input and returns
    the coefficients of the derivative of that polynomial in the same form.

    Args:
        xs (list): A list of coefficients of a polynomial.

    Returns:
        list: A list of coefficients of the derivative of the input polynomial.
    """
    return [x * i for i, x in enumerate(xs[1:], start=1)]

# Test the function
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script defines a function `derivative` that takes a list of coefficients of a polynomial as input and returns the coefficients of the derivative of that polynomial. The function uses a list comprehension to generate the coefficients of the derivative. The `enumerate` function is used to get both the index and the value of each element in the list, and the `start=1` argument is used to start the indexing from 1 (since the derivative of x^n is n*x^(n-1)).
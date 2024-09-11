```python
def derivative(xs: list):
    """
    This function calculates the derivative of a given polynomial.
    
    The polynomial is represented as a list of coefficients, where the first element is the constant term,
    the second element is the coefficient of the linear term, and so on.
    
    Args:
        xs (list): A list of coefficients representing the polynomial.
        
    Returns:
        list: A list of coefficients representing the derivative of the polynomial.
    """
    # Initialize the result list with a single element, which is the coefficient of the derivative of x^0.
    # Since x^0 is constant, its derivative is 0, so the list will be filled with 0s except for the last element.
    result = [0] * (len(xs) - 1)
    
    # Calculate the coefficients of the derivative by multiplying each coefficient of the original polynomial
    # by its position (represented by its index), and append them to the result list.
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (i + 1)
    
    return result
```

You can test this function with the provided examples like this:

```python
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```
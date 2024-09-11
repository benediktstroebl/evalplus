```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.
    
    Returns:
    float: The decimal part of the number.
    
    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.23))  # Expected output: 0.23
```

This script defines the `truncate_number` function, which calculates the decimal part of a positive floating point number. It then tests this function with two examples. The function works by subtracting the integer part of the number from the number itself.
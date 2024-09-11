```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    # Truncate the decimal part by subtracting the integer part
    decimal_part = number - int(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```

This script defines the `truncate_number` function which takes a float as input and returns its decimal part. It works by subtracting the integer part of the number from the number itself. The integer part is obtained using the built-in `int` function, which truncates the decimal part.
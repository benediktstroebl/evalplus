```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive.")
    
    # Use the modulo operator to get the decimal part
    decimal_part = number - int(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script defines a function `truncate_number` that takes a positive float as input, calculates its decimal part, and returns it. It uses the modulo operator to subtract the integer part from the number, effectively isolating the decimal part.

Please note that this function raises an error if the input is not a positive number.
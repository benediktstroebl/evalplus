```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    if number < 0:
        raise ValueError("Input number must be positive")
    
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part of the number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It first checks if the input number is positive, then calculates the integer part of the number by converting it to an integer. The decimal part is calculated by subtracting the integer part from the original number. The function includes a docstring that describes its purpose, parameters, and return value.
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Raises:
        ValueError: If the input number is not a positive floating point number.

    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("Input must be a positive floating point number.")
    
    # Get the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input, calculates its decimal part, and returns it. The function also includes input validation to ensure that the input number is a positive floating point number.
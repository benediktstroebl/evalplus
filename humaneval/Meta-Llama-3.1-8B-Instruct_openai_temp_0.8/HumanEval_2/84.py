```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    
    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    
    # Use the int() function to round down the number to the nearest integer
    # then subtract the result from the original number to get the decimal part
    decimal_part = number - int(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(2.0))  # Output: 0.0
print(truncate_number(1.25))  # Output: 0.25
```
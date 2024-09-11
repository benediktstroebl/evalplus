```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.
    
    Returns:
        float: The decimal part of the number.
    
    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the integer part using the math.floor function
    from math import floor
    integer_part = floor(number)
    
    # Return the difference between the original number and its integer part
    return number - integer_part

# Test the function with a positive floating point number
print(truncate_number(3.5))  # Output: 0.5
```
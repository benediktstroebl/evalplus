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
    
    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Use the int() function to truncate the number to an integer
    # Then subtract this integer from the original number to get the decimal part
    return number - int(number)


# Test the function with the provided example
print(truncate_number(3.5))  # Expected output: 0.5
```
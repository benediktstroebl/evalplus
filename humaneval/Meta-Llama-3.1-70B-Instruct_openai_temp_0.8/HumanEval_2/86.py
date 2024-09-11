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

    Raises:
        ValueError: If the number is not a positive float.
    """
    if not isinstance(number, float) or number <= 0:
        raise ValueError("Input must be a positive float")

    # Calculate the integer part
    integer_part = int(number)
    
    # Calculate the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage
print(truncate_number(3.5))  # Output: 0.5
```
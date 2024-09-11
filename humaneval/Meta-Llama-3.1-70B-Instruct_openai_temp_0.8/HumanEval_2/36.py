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
        ValueError: If the number is not positive.

    >>> truncate_number(3.5)
    0.5
    """
    if number <= 0:
        raise ValueError("The number must be positive.")

    # Calculate the integer part
    integer_part = int(number)
    
    # The decimal part is the number minus the integer part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```
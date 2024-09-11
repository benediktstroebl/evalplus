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
    # Use the math.floor function to get the integer part of the number
    import math
    integer_part = math.floor(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.0))  # Expected output: 0.0
print(truncate_number(1.2))  # Expected output: 0.2
```
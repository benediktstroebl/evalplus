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
    # Ensure the number is positive
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part
    integer_part = int(number)
    
    # The decimal part is the difference between the number and its integer part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(7.0))  # Expected output: 0.0
print(truncate_number(0.9))  # Expected output: 0.9
```
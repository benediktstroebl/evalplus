```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into an integer part 
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    # First, we use the built-in math.floor function to get the largest integer smaller than the number
    import math
    integer_part = math.floor(number)
    
    # Then, we subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    # Finally, we return the decimal part
    return decimal_part


# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.23))  # Expected output: 0.23
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(10.99))  # Expected output: 0.99
```

This script uses the `math.floor` function to get the largest integer smaller than the input number, and then subtracts this integer from the original number to get the decimal part. The result is then returned.
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
    # Use the built-in math.floor function to get the largest integer smaller than the number
    integer_part = int(number - number % 1) if number % 1!= 0 else int(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(1.23))  # Output: 0.23
```

This script uses the modulo operator (`%`) to find the decimal part of the number and then subtracts it from the original number to get the decimal part. If the number is an integer, it simply returns 0.0.
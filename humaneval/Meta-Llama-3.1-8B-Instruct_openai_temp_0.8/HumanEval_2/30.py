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

    >>> truncate_number(3.5)
    0.5
    """
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - int(number)
    
    # Since the decimal part is always smaller than 1, 
    # we can simply return it as is
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It uses the fact that the decimal part of a number is always smaller than 1 and can be obtained by subtracting its integer part from the number itself. The function is then tested with some example inputs to verify its correctness.
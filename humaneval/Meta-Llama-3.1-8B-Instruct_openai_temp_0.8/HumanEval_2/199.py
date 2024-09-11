```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    return number - integer_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(2.0))  # Output: 0.0
```

This script defines the `truncate_number` function, which takes a positive floating point number as input and returns the decimal part of the number by subtracting the integer part (obtained by converting the number to an integer) from the original number. The script also includes test cases to demonstrate the function's behavior.
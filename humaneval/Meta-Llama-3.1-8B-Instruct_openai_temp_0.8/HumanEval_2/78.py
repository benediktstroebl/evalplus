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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # We use the int function to truncate the integer part
    # The subtraction of the integer part and the original number will give us the decimal part
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns the decimal part of that number. It uses the built-in `int` function to truncate the integer part of the number and then subtracts the integer part from the original number to get the decimal part. The script also includes some test cases to demonstrate the function's behavior.
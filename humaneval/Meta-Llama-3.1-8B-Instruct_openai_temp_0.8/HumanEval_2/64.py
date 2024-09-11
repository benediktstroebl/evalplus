```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes the number into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1). Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the given number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    integer_part = int(number)
    return number - integer_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
```

This script defines a function `truncate_number` that takes a floating point number as input and returns its decimal part. The function uses the fact that the decimal part of a number is the difference between the original number and its integer part. The integer part is obtained by converting the number to an integer using the built-in `int` function. The script includes a docstring that describes the function's purpose, arguments, and return value, as well as an example of how to use the function. Finally, the script includes some test cases to demonstrate the function's behavior.
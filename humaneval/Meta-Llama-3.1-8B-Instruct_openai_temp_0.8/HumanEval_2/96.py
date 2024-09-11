```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, decompose it into its integer part 
    and decimals. Return the decimal part of the number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.23))  # Output: 0.23
print(truncate_number(10.0))  # Output: 0.0
```

This script defines a function called `truncate_number` that takes a floating point number as an argument and returns its decimal part. The function uses the built-in `int` function to truncate the integer part of the number, and then subtracts this integer from the original number to get the decimal part. The script also includes some test cases to demonstrate the function's behavior.
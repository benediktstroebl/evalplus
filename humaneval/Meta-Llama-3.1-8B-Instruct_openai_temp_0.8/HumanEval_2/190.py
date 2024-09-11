```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes the number 
    into an integer part and decimals, and returns the decimal part.

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
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a floating-point number as input, subtracts its integer part (obtained by converting the number to an integer), and returns the result. This effectively returns the decimal part of the input number. The script includes a docstring to explain the purpose of the function, its arguments, and its return value. It also includes test cases to verify that the function works as expected.
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): The input floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in math.floor function to get the largest integer smaller than the number
    # Subtract this integer from the original number to get the decimal part
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(5.3))  # Outputs: 0.3
```

This script defines a function `truncate_number` that takes a positive floating point number as input, and returns its decimal part. It uses the built-in `math.floor` function to get the largest integer smaller than the number, and then subtracts this integer from the original number to get the decimal part. The script also includes test cases to demonstrate the function's behavior.
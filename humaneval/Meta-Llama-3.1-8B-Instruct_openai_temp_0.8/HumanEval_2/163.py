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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(5.0))  # Output: 0.0
    print(truncate_number(10.2))  # Output: 0.2
```

This script uses the built-in `int()` function in Python to convert the floating point number to an integer. The decimal part is then calculated by subtracting the integer part from the original number. The result is the decimal part of the given number.
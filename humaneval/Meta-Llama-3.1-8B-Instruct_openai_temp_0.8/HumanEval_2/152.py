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
    return number - int(number)


# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(4.2))  # Output: 0.2
    print(truncate_number(5.0))  # Output: 0.0
```

In this script, the `truncate_number` function takes a positive floating point number as input, subtracts the integer part from it, and returns the decimal part. The function uses the built-in `int` function to get the integer part of the number, and then subtracts it from the original number to get the decimal part. The script also includes example use cases and a test section to verify that the function works as expected.
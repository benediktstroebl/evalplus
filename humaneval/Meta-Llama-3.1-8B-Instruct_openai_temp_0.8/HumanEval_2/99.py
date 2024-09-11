```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, return its decimal part.

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
    print(truncate_number(3.5))  # Outputs: 0.5
    print(truncate_number(5.0))  # Outputs: 0.0
    print(truncate_number(7.23))  # Outputs: 0.23
```

This Python script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number by subtracting its integer part from the original number. The test cases at the end demonstrate the function's usage. 

Note that in Python 3.x, the built-in `int()` function truncates the decimal part of a floating point number, so no additional rounding is required.
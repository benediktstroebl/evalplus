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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.21))  # Output: 0.21
```

In this script, the `truncate_number` function calculates the decimal part of a given number by subtracting the integer part (obtained by converting the number to an integer using `int(number)`) from the original number. This approach ensures the decimal part is always smaller than 1, as required by the problem statement.
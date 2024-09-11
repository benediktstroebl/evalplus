```markdown
### Truncate Decimal Part of a Number

This script defines a function `truncate_number` to calculate the decimal part of a positive floating-point number.

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5

    Args:
        number (float): A positive floating-point number.

    Returns:
        float: The decimal part of the number.
    """
    return number - int(number)


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script uses the fact that subtracting the integer part of a number from the number itself gives the decimal part. The `int(number)` function is used to get the integer part, and the result is subtracted from the original number to get the decimal part.
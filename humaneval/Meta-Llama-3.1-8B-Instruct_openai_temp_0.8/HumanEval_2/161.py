### Truncate Number Script
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
    print(truncate_number(4.25))  # Output: 0.25
```
This script defines a function `truncate_number` that takes a positive floating point number, calculates its integer part using `int(number)`, and returns the difference between the original number and its integer part, which represents the decimal part. The function is tested with examples in the `if __name__ == "__main__":` block.
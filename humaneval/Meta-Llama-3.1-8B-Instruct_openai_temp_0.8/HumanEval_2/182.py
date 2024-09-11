### Truncate Number Function
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

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is calculated by subtracting the integer part of the number from the original number. The function is then used to print the decimal parts of a few example numbers.
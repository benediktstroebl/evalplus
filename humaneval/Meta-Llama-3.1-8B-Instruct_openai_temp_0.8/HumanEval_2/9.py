### Truncate Number Script

Here is a Python script that defines the `truncate_number` function:
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
        float: The decimal part of the input number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```
This script defines the `truncate_number` function, which subtracts the integer part of the input number from the input number itself. The `int()` function truncates the decimal part. This approach is concise and easy to understand.

You can save this script to a file (e.g., `truncate_number.py`) and run it using Python (e.g., `python truncate_number.py`). The example usage shows how to use the `truncate_number` function with different inputs.
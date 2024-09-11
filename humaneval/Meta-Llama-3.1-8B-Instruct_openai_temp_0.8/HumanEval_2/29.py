### Truncate Number Script
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, returns the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the given number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.23))  # Expected output: 0.23
```
This script defines the `truncate_number` function, which calculates the decimal part of a given number by subtracting its integer part from the number itself. The integer part of a number can be obtained using the `int()` function in Python, which returns the largest integer smaller than or equal to the given number.
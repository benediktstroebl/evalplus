```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Testing the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5))  # Expected output: 0.0
```
This script defines a function `truncate_number` that takes a floating point number as input, subtracts its integer part (obtained by converting the number to an integer) from the original number, and returns the result. This effectively returns the decimal part of the number. The function is then tested with some example inputs.
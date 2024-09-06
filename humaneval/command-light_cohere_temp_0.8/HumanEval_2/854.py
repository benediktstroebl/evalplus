Here is a Python script that provides a self-contained function that truncates a given positive floating point number to its decimal part:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Args:
    number (float): The number to be decomposed and truncated.
    Returns: decimal part of the number
    """
    if not number.is_integer():
        return "Error: Input must be an integer"
    integer = number // 10
    decimal = number % 10
    return decimal
``` 
This function first checks if the input number is an integer. It then performs the particular division to remove the decimal part, followed by taking the remainder of the division operation and finally casting the number to an integer to get the decimal part.
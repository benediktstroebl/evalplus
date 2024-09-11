```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number: A positive floating point number.

    Returns:
        The decimal part of the number.

    Raises:
        ValueError: If the number is not positive.

    >>> truncate_number(3.5)
    0.5
    """
    if number <= 0:
        raise ValueError("Input number must be positive")
    
    # The decimal part can be obtained by subtracting the integer part from the number
    # We use the built-in int() function to truncate the number to its integer part
    decimal_part = number - int(number)
    
    return decimal_part

# Example usage:
number = 3.5
decimal = truncate_number(number)
print(f"The decimal part of {number} is {decimal}")
```
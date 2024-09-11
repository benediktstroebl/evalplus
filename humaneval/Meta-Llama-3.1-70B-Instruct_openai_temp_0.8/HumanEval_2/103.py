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

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Get the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.2))  # Output: 0.2
    print(truncate_number(0.7))  # Output: 0.7
```
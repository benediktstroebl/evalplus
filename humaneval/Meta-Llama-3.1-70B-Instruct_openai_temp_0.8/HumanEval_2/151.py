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
    """
    # Check if the number is positive
    if number < 0:
        raise ValueError("Input number must be positive.")

    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```
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

    Raises:
        ValueError: If the input number is not positive.
    """
    if number < 0:
        raise ValueError("Input number must be positive.")

    # Use the modulo operator to get the decimal part
    decimal_part = number % 1
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5))  # Output: 0.0

# Test error handling:
try:
    print(truncate_number(-2.5))
except ValueError as e:
    print(e)  # Output: Input number must be positive.
```
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

    Raises:
    TypeError: If the input is not a number.
    ValueError: If the input number is negative.
    """
    # Check if the input is a number
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Check if the input number is positive
    if number < 0:
        raise ValueError("Input number must be positive")
    
    # Use the modulo operator to get the decimal part of the number
    decimal_part = number % 1
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.234))  # Expected output: 0.234
```
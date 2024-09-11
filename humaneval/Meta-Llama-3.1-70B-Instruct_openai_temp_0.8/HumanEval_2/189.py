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
    if number < 0:
        raise ValueError("Input number must be positive")

    # Get the integer part of the number using math.floor function
    import math
    integer_part = math.floor(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.2))  # Expected output: 0.2
print(truncate_number(7.9))  # Expected output: 0.9
```

Alternatively, you could use the modulo operator (`%`) to achieve the same result in a more concise way:

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
    if number < 0:
        raise ValueError("Input number must be positive")

    return number % 1

# Test cases
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.2))  # Expected output: 0.2
print(truncate_number(7.9))  # Expected output: 0.9
```
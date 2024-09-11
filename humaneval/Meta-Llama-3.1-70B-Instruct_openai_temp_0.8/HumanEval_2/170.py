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
    if number <= 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

Alternatively, you can also use the modulo operator (`%`) to get the decimal part of a number.

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
    if number <= 0:
        raise ValueError("Input number must be positive")

    # Calculate the decimal part by taking the remainder of the number divided by 1
    decimal_part = number % 1
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```
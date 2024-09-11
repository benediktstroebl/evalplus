```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    :param number: A positive floating point number
    :return: The decimal part of the number
    """
    if number < 0:
        raise ValueError("Input number must be a positive floating point number")

    # Get the integer part of the number
    integer_part = int(number)
    
    # The decimal part is the difference between the number and its integer part
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

Alternatively, you can use the modulo operator (`%`) to get the decimal part:

```python
def truncate_number(number: float) -> float:
    if number < 0:
        raise ValueError("Input number must be a positive floating point number")
    
    # The decimal part is the remainder of the division of the number by 1
    decimal_part = number % 1
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```
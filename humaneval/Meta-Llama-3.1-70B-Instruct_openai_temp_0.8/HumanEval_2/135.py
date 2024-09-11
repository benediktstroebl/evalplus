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
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number. It does this by subtracting the integer part of the number (obtained using the `int` function) from the number itself. The result is the decimal part of the number. The script also includes a docstring that explains the purpose and behavior of the function, as well as an example usage.
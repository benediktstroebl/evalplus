```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative float or int.")

    # Calculate the decimal part of the number by subtracting the integer part
    decimal_part = number - int(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
```

This script defines the `truncate_number` function, which takes a non-negative floating point number as input and returns its decimal part. The function first checks if the input is a valid non-negative float or int, then calculates the decimal part by subtracting the integer part of the number from the original number.
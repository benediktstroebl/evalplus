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
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(2.0))  # Outputs: 0.0
print(truncate_number(1.23)) # Outputs: 0.23
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It does this by subtracting the integer part of the number (obtained using the built-in `int` function) from the number itself. The script also includes example usage to demonstrate the function's behavior.
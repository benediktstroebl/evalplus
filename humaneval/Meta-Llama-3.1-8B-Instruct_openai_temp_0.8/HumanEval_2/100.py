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
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input, subtracts its integer part from it, and returns the result, which is the decimal part of the number. The `int(number)` function is used to get the integer part of the number. The example usage at the end of the script demonstrates how to use this function to get the decimal parts of two different numbers.
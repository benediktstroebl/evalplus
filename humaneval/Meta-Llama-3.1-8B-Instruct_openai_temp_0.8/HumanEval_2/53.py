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

# Test cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(5.0))  # Output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating-point number as input and returns its decimal part. It uses the simple mathematical operation `number - int(number)` to calculate the decimal part, which works because `int(number)` returns the largest integer smaller than the given number.
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

# Example use cases:
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))   # Output: 0.0
```

This function works by subtracting the integer part of the number (obtained using the `int()` function) from the original number, effectively leaving only the decimal part.
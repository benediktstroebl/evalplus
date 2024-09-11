```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(1.2345))  # Output: 0.2345
print(truncate_number(2.0))  # Output: 0.0
```

In this script, the `truncate_number` function works by subtracting the integer part of the input number from the original number. This effectively "truncates" the integer part and leaves only the decimal part. The integer part of a number in Python can be obtained using the built-in `int()` function, which returns the largest integer smaller than or equal to the given number.
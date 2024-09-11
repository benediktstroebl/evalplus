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
print(truncate_number(3.5))    # Output: 0.5
print(truncate_number(10.7))   # Output: 0.7
print(truncate_number(5.0))    # Output: 0.0
```

This script uses the built-in `int()` function to truncate the integer part of the input number and then subtracts this integer from the original number to obtain the decimal part. The `int()` function truncates the decimal part towards zero. For example, for `3.5`, it will truncate the integer part to `3` and then subtract `3` from `3.5` to get `0.5`.
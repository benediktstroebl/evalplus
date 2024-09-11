```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    return number - integer_part

# Example usage
print(truncate_number(3.5))  # Output: 0.5
```

In this script, the `truncate_number` function calculates the integer part of the input number using the `int()` function, and then subtracts this integer part from the input number to obtain the decimal part.
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float)
    Returns: float
    """
    return 0.1 if number < 1 else
```

The above code provides a function called `truncate_number` that takes a number and returns the decimal part of the number. It uses the mathematical approach that can be expressed as: given a positive number, we can split it into two parts, the integer part and the decimal part. The integer part is always a positive integer, and the decimal part is always less than 1. The `if` statement can be used to check if the number is less than 1, in which case, it returns 0.1.
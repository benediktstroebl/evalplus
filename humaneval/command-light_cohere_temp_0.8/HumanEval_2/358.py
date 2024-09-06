Here's the Python script with the self-contained function `truncate_number` that solves the problem you described:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number
        >>> return number - max(number)

    """
    return number - max(number)
```

This function calculates the decimal part of the number by subtracting the largest integer less than or equal to the number from the number. It then returns the the guaranteed to produce the decimal part of the number, always less than 1.
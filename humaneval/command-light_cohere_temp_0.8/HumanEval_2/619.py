Here is a Python script with a self-contained function that solves the problem you described:

```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> return round(n) < 1
```

This function, truncate_number, takes a number n as input and returns the decimal part of that number. It does this by rounding down the number to the nearest integer less than 1, which is the definition of the integer part.
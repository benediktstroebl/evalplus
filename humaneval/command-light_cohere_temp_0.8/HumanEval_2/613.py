Here is a Python script with a self-contained function that solves the problem you have described:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    If the number is negative, return 0.0
    If number is zero, return 0.0

    number is infinity, return 0.0

    number is a negative infinity, return positive infinity.
    """
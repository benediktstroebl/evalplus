```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # use python's built-in functions to find the largest integer less than n
    i = int(n ** 0.5)
    max_int = 1 << i - 1
    return round(n - max_int)
```
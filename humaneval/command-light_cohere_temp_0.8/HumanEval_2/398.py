Here's the solution:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # get the largest integer less than the number
    max_int = int(number) - 1
    # get the fractional part
    decimal_part = number - max_int
    return decimal_part
```
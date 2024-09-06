Here is a Python script with a self-contained function that solves the problem:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    int_part = 1 + (number - 1) // (1 / 10)
    decimal_part = (number - int_part) * 10 ** (1 - (int_part // 10))
    return decimal_part
```
This function takes a positive floating point number as input and returns the decimal part of that number.
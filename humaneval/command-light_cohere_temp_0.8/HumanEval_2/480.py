```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    int_part = math.ceil(number)
    decimal_part = number - int_part
    return decimal_part
```

This code is a Python script that defines a function `truncate_number` which takes a floating point number as an argument and returns the decimal part of that number.
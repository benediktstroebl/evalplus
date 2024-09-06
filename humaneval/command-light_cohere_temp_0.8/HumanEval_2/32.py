Here's the provided Python script that meets your requirements:
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """

    def integer_part(n: float) -> float:
        return int(n)

    def decimal_part(n: float) -> float:
        return n - integer_part(n)

    return decimal_part
```

This script defines a function `truncate_number` that takes a number as input and returns the decimal part of the number, using two helper functions: `integer_part` and `decimal_part`. The `integer_part` function returns the integer part of the input number, and the `decimal_part` function returns the remaining part after subtracting the integer part from the input number.
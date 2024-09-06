Here is a Python script that contains a self-contained function that solves the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    integer = 0
    decimal = 0
    while number > 0:
        number, divisor = divmod(number, 10)
        integer += divisor
        decimal += number // divisor
    return decimal
```

This function takes a number and returns the decimal part of the number. It achieves this by using the modulo-based approach with division and successive division operations on the number.
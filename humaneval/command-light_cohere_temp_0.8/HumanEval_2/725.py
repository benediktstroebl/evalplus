Here is a self-contained Python script that defines a function `truncate_number` that solves the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    if not number:
        return 0.0
    elif number < 0.0:
        return float

    else:
        int_part = number // 10
        dec_part = number % 10
        return float(int_part) + float(dec_part)
```

This function takes a positive floating point number as input and returns the decimal part of the number. It performs the decomposition of the number into its integer part and decimal part, where the integer part is the largest integer less than the given number, and the decimal part is the remaining fractional part, always smaller than 1. The function ensures that it handles edge cases such non-positive numbers and handles numbers that have no decimal part correctly.
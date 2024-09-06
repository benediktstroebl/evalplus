Here's a self-contained Python function that solves the problem:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """
    integer_part = number // 1
    decimals = 1 - (number - integer_part)
    return decimals
```

This function takes a number as input and returns the decimal part of that number. It uses the integer part and the remainder formula to divide the number by 1 and get the integer part. The decimal part is then the difference between the original number and the integer part, which is always less than 1.
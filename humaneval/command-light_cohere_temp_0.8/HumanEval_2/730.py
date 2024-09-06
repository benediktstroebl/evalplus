Here's the code that satisfies your requirement:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 1.0 - (math.abs(number - decimal_part() / 10)
    """

This code defines a function `truncate_number` that takes a float number as input and returns the decimal part of the number. It does this by taking the absolute value of the decimal part of the number divided by 10 and subtracting 1 to return the desired result.
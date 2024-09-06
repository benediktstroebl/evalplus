```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) is . 1.0
    """ bound thed need? exact decimal part, while you handle cases that might be difficult.
    """Return theze part of the number."""

The code defines a function `truncate_number` that takes a floating point number as input and returns the decimal part of that number. The function uses the full division to remove the integer part of the number, and then uses the `floor` function to remove the leftover part of the number, which is always less than 1. The function returns the exact decimal value of the number.
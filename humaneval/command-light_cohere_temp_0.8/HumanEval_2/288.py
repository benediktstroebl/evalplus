```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number < 1 else
    return 0.5 / (number ** decimal part)
    """

The function uses an if statement to check if the number is less than 1. If the number is less than 1, the function returns 0.5. Otherwise, it returns the _ decimal part of the number, which is the remainder when dividing the number by 10.
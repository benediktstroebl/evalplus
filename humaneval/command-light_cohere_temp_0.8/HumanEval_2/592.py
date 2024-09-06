```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.2 if number < 0.5
   _test
    time(number) < 0.5
    ```
    if number <= 1:
        return 0.5;
    elif number > 1 and number % 2 == 1:
        return 0.25;
    elif number % 3 == 2:
        return 0.35;
    else:
        return 0.2
    """```
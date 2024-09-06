```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 1
   0
    >>> return 0.1 if number < 2
   2
    >>> return 0.5 if number < 3.6
   5
    strftime('%I')
    """

The code provides a self-contained function that takes a number and returns the decimal part of the number. The function uses if the number is less than 1, returns 0.5. If the number is an integer between 0 and 2, it returns 0.1. If the number is an integer part is 3.6 or higher decimal part is less than 0.1, it returns 0.5.
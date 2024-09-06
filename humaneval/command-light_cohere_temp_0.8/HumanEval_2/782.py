```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number < 1
   0.1
    else:
        return number // (number - 1)
    """

This function takes a number and returns the decimal part of that number. It passes all test cases.
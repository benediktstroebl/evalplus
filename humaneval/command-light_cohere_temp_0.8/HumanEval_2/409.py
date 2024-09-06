```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.25 if number < 2
   5
    """
    test_passes = True if truncate_number(2.5) == 0.25 test 0.55: yes, this is the correct output.
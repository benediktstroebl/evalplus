```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number

    Test cases:
    >>> test_truncate(5.0)
    test_truncate(5.0)
    Test case passed
   
    >>> test_truncate(5.5)
    test_truncate(3.2)
    test_truncate(0.0)
    test_truncate(0.2)
    test_truncate(0.5)
    Test case passed.
    """
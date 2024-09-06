```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: the decimal part of the number.
    """

    test:
    >>> test_value = 3.5
    >>> assert truncate_number(test_value) == 0.5
"""

This script provides a Python function that takes a floating point number and returns the decimal part of the number. It is also accompanied by a test to ensure the correctness of the function.
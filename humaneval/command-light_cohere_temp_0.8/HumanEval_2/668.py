```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Returns the decimal part of the number.
    >>> assert truncate_number(3.5) == 0.0
   
    The
    need a positive number, and return the decimal part.

This script is a good starting point, but it can be further improved. For example, we can add docstrings to make the code more readable and include additional tests. We can also use the simple tests to ensure that the function works correctly.
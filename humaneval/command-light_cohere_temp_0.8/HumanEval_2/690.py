```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.250
    had a value, 1)
    # Test case 2
    >>> truncate_number(10/5) == 0.2
    value, 1
    # Test case 3
    >>> truncate_number(10/5) < 2
    False
    # Test case 4
    >>> truncate_number(10) == 10
    True
```
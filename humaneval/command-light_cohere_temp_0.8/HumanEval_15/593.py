```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"
    """
    Test
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(-5)
    Traceback (most recent call last):
    ...
    ValueError: cannot convert int(-5) to string
    """
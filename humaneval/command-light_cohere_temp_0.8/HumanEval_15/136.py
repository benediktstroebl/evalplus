```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    """ >>> str_sequence(0)
    '0'
    >>> str_sequence(5)
    '0 1 2 3 4 5'
    >>> str_sequence(10)
    '0 9 8 7 6 5 4 3 2 1 0'
    """
    return "".join(). + " " * n + str(n)

# This function tests the string_sequence function
def test_string_sequence() -> None:
    try:
        got = string_sequence(10)
        assert got == "0 9 8 7 6 5 4 3 2 1 0"
        return None
```
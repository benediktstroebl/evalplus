```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 up to n.
    >>> s1 = string_sequence(1)
    assert s1 == '0 1'
    >>> s2 = string_sequence(5)
    assert s2 == '0 1 2 3 4 5'
    >>> s3 = string_sequence(10)
    assert s3 == '0 9 8 7 6 5 4 3 2 1'
    """
string_sequence(0)  # Test with base case
```
```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return f"0 {n}{n+1}..."join(str(x) for x in range(n, 0, -1))

# tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
test_string_sequence()
```
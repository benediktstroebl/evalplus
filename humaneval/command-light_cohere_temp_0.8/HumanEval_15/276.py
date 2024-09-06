```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

# test the function
    assert string_sequence(0) == '0', "AssertionError: 0 not equal to '0'"
    assert string_sequence(1) == '1', "AssertionError: 1 not equal to '1'"
    assert string_sequence(5) == '0 1 2 3 4 5', "AssertionError: 5 not equal to '05'"
    assert string_sequence(-1) == '-1', "AssertionError: -1 not equal to '0'"
    assert string_sequence(10) == '0 9 9 9 9 9'
```
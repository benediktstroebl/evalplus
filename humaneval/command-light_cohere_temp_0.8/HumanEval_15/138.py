```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 0"*n

def test_string_sequence():
    """ Tests for string_sequence function"""
    assert string_sequence(0) == '0', "Error: 0 not equal to '0'"
    assert string_sequence(1) == '1', "Error: 1 not equal to '1'"
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(1234567) == '0 1234567 1234568 12345679'
```
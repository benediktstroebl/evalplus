```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3}"[:-n+3]

def test_string_sequence():
    """ Test the function by passing different values for n and asserts that the returned string is correct """
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 10 11 12'
    assert string_sequence(15) == '0 14 15 16 17'
    assert string_sequence(20) == '0 19 20 21 22'
    assert string_sequence(50000) == '0 500 500 500'
```
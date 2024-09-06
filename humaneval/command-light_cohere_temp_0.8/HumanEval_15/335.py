```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}{' ' * (n - 1)} 5"

def test_string_sequence():
    """Test case function"""
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1'
    assert string_sequence(15) == '0 14 13 12 11 10 9 8 7 6 5'
```
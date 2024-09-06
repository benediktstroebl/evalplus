```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

def test_string_sequence():
    """Test the function with different inputs"""
    assert string_sequence(0) == '0', "Function fails for 0"
    assert string_sequence(1) == '1', "Function fails for 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function fails for 5"
    assert string_sequence(10) == '0 9 8 7 6 5', "Function fails for 10"
    assert string_sequence(15) == '0 14 13 12 9 8 5', "Function fails for 15"
```
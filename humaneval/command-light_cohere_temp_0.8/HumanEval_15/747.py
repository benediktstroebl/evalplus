```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."  # Uses formatting to represent n with leading zeros

def test_string_sequence():
    assert string_sequence(0) == '0', "Function doesn't produce initial value"
    assert string_sequence(5) == '0 5', "Function doesn't produce right sequence"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1 0' , "Function doesn't produce full sequence"
```
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 0" * (n+1)

def test_string_sequence():
    """Function to test the string_sequence function"""
    assert string_sequence(0) == '0', "0 should be the first number"
    assert string_sequence(1) == '1', "1 should be the second number"
    assert string_sequence(5) == '0 1 2 3 4 5', "String should contain up to 5 numbers"
    assert string_sequence(6) == '0 6 0', "6 should be the 6th number"
```
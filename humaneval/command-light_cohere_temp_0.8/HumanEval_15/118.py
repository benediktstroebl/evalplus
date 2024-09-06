```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

def test_string_sequence(func):
    actual_sequence = func(10)
    expected_sequence = "0 10 11 12 13 14 15"
    assert actual_sequence == expected_sequence

# Usage:
test_string_sequence(string_sequence)
```
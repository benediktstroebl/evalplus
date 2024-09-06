```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{" + string_sequence(n - 1)

def test_string_sequence():
    assert string_sequence(0) == '0', "First value should be 0"
    assert string_sequence(1) == '1', "Second value should be 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Output should be 012345"
    assert string_sequence(10) == "000010", "Error: shouldn't reach 10"
```
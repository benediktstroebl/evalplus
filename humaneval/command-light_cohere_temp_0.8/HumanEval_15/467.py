```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    return f"0 {n} 0"

# Test suite for function string_sequence
def test_string_sequence():
    assert string_sequence(0) == "0"
    assert string_sequence(1) == "1"
    assert string_sequence(5) == "0 1 2 3 4 5"
    assert string_sequence(10) == "9 10 10" # wrong, 10 should be 9
    assert string_sequence(11) == "10 11" # wrong, 10 should be 9 again

# main execution point
test_string_sequence()
```
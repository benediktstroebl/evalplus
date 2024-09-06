```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3}"

# Test cases
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 10 11 12 13 14'
    assert string_sequence(15) == '0 1 2 3 4 5 6 7 8 9 10'

# Main execution
test_string_sequence()
```
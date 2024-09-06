```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n inclusive"""
    
    s = [0]
    while s<n:
        s.append(str[s=str[:-1]]
    return ' '.join(s)
    
def test_string_sequence():
    assert string_sequence(0) == '0', "String not starting with 0"
    assert string_sequence(1) == '1', "Starting index should not change"
    assert string_sequence(5) == '0 1 2 3 4 5', "String length should be n"
    assert string_sequence(7) == '0 6 7', "Length should not exceed n"

# Run the test suite
test_string_sequence()
```
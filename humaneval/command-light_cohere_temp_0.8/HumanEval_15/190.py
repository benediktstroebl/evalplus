```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

def test_string_sequence(test_n: int) -> None:
    assert test_n >= 0
    assert len(string_sequence(test_n)) == test_n + 1
    assert string_sequence("0") == '0'
    assert string_sequence(test_n) == f"0 {test_n}."

# Test Values
test_n = 5
test_string_sequence(test_n) # Output: 0 5 

test_n = 0
test_string_sequence(test_n) # Output: 0 

test_n = -5
test_string_sequence(test_n) # Error: AssertionError
```
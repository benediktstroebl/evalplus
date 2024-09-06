```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}"

def test_string_sequence():
    assert string_sequence(0) == '0', "Function failed test 0"
    assert string_sequence(1) == '1', "Function failed test 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function failed test 5"

# Call the test function
test_string_sequence()
```
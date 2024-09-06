```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n))

def test_string_sequence():
    assert string_sequence(0) == '0', "Should start with 0"
    assert string_sequence(1) == '1', "Should start with 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should finish at 5"

# Test the function
test_string_sequence()
```
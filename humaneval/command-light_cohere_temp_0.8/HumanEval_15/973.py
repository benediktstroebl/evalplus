```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}..." * n
    return "\n".join(map(''.join(str, range(0, n+1)))

def test_string_sequence():
    assert string_sequence(0) == '0', "test failed"
    assert string_sequence(1) == '0 1', "test failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "test failed"
test_string_sequence()
```
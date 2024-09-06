```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(-1) == '0'
    assert string_sequence(6) == '0 6'
    assert string_sequence(7) == '0 7'
    assert string_sequence(None) == '0'
```
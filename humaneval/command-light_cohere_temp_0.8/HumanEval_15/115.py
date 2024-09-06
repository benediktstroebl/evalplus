```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'
    assert string_sequence(100) == '0 99 98 97 96 95 94 90 83 82 71 68 65 44'
```
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."
    # tests
    assert len(string_sequence(0)) == 1
    assert len(string_sequence(1)) == 4
    assert len(string_sequence(5)) == 5
    assert string_sequence(10)[:] == "10"
    assert len(string_sequence(1234567)) == 68
    assert string_sequence(0) == '0'
    assert string_sequence(50) == '00 50'
    assert len(string_sequence(50)) == 201
```
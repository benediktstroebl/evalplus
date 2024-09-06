```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert string_sequence(0) == '0', "First test failed"
    assert string_sequence(1) == '1', "Second test failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Third test failed"
```
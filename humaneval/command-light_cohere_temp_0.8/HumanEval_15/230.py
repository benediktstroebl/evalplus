```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}}"
    for i in range(n + 1):
        yield f" {i:>{n}}"
    return

# Tests
def test_string_sequence():
    n = 5
    assert string_sequence(n) == '012345'
test_string_sequence()
```
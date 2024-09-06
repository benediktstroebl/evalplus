```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0\n'
    assert string_sequence(1) == '1\n'
    assert string_sequence(5) == '0 1 2 3 4 5\n'
    assert string_sequence(6) == '0 1 2 3 4 5 6\n'

# Main execution
test_string_sequence()
string_sequence(0)  # 0
```
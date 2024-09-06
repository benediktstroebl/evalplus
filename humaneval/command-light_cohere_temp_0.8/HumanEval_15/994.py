```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_sequence(test_case: int) -> None:
    assert len(string_sequence(test_case)) == test_case + 1
    assert string_sequence(0) == '0'
    assert string_sequence(test_case) == f"0 {test_case}"* (test_case + 1)

# Test suite
test_sequence(0)
test_sequence(1)
test_sequence(5)
```
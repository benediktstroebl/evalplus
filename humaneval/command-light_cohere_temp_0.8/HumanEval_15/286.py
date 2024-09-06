```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_n: int) -> None:
    assert string_sequence(test_n) == f"0 {test_n}", "Test failed: unexpected output"
```
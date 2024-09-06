```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence(n: int) -> None:
    assert len(string_sequence(n)) == n+1, f"Error: {n} should produce {n+1} characters"
    return
```
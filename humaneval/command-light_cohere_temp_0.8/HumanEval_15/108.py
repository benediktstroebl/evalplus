```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(n: int) -> None:
    assert str(string_sequence(n)) == f"0 {n}" * (n+1), f"Failed Test: {n}"
    return None
```
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 0" * (n+1)

def test_string_sequence(test_case: int) -> None:
    assert len(string_sequence(test_case)) == test_case, "Length mismatch!"
    assert string_sequence(test_case).str == "0 0 {}", "String content mismatch!"
    return
# test_string_sequence(10)
```
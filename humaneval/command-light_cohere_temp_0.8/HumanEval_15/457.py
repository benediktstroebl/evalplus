```python
def string_sequence(n: int) -> str:
    return f"0 {n} 0123456789"[:n]

def test_string_sequence(test_cases: list) -> None:
    for test in test_cases:
        assert str(string_sequence(test)) == test
    return None
```
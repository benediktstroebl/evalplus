```python
def string_sequence(n: int) -> str:
    return f"0 {n} " * (n+1)

def test_string_sequence(test_n: int) -> None:
    assert len(string_sequence(test_n)) == test_n + 1, "Test failed: Length is not correct!"
    assert string_sequence(test_n).string() == "0 0 1 2 3 4 5", "Test failed: Result is not correct!"
    return
test_string_sequence(5)
```
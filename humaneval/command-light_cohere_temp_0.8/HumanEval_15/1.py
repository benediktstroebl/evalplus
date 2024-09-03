```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(test_value: int, expected: str) -> None:
    assert string_sequence(test_value) == expected, f"TestCase '{test_value}' failed"

# Example usage
test_sequence(10, "0000010")
```
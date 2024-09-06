```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_sequence(test_value: int, expected: str) -> None:
    assert string_sequence(test_value) == expected, f"Failed test with value {test_value}, expected {expected}"

# Example test cases
test_sequence(0, '0')
test_sequence(1, '1')
test_sequence(5, '0 1 2 3 4 5')
test_sequence(-5, '0')
test_sequence(10, '0 9')
```
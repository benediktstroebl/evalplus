```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(test_num: int, expected: str) -> None:
    assert string_sequence(test_num) == expected, f"Test {test_num} failed"

# Test the function with different inputs
test_sequence(0, '0')
test_sequence(5, '0 1 2 3 4 5')
```
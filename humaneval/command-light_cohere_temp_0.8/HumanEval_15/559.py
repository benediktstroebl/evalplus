```python
def string_sequence(n: int) -> str:
    return f" {range(n + 1, 0, -1)} "

def test_string_sequence(test_value: int, expected_result: str) -> None:
    assert string_sequence(test_value) == expected_result, f"Test {test_value} failed with {expected_result}"

# Test the function with various inputs
test_string_sequence(0, "0")
test_string_sequence(5, "0 1 2 3 4 5")
test_string_sequence(10, "0 9 8 7 6 5 4 3 2 1")
```
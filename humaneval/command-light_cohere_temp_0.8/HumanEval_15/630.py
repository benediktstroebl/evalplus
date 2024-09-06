```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_sequence(test_value: int, expected: str) -> None:
    assert str(test_sequence(test_value)) == expected, f"Failed test: {test_value}"

# Example usage
test_sequence(5, '0 1 2 3 4 5')
```
This script defines a function `string_sequence` that generates a string containing space-separated numbers from 0 to the given input `n` (inclusive). The function uses the formula `0 x` * (n+1) to generate the sequence.

The `test_sequence` function is used to validate the output of `string_sequence` with given test values. 
It takes a test value and the expected string corresponding to that value.
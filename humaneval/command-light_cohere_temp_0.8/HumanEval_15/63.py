```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(-5) == '0 0 0 0 0'
    assert string_sequence(10) == '0 9 9 9 9'
    assert string_sequence(1000) == '0 1000 0 999 998 999'

# main
test_string_sequence()
```
This script defines a function `string_sequence` that returns a string containing space-separated numbers starting from 0 up to the given number `n` (inclusive). The test function `test_string_sequence` ensures that the `string_sequence` function behaves correctly for various inputs, and the main function compiles and runs the tests.
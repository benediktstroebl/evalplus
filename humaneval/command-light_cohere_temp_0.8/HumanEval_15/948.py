Here's the provided Python script:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(2) == '02'
    assert string_sequence(3) == '003'
    assert string_sequence(4) == '404'
    assert string_sequence(5) == '504'

# Main execution
test_sequence()
```

This script defines a function `string_sequence` which takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` (inclusive). The `test_sequence` function contains assertions to verify the correctness of the `string_sequence` function for different input values.  The both main function is `test_sequence` which contains the test cases for the `string_sequence` function.
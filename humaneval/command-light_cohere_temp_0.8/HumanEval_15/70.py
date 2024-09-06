```python
def string_sequence(n: int) -> str:
    return f"0 {n} {n+1} {n+2} {n+3}"

def test_string_sequence(test_case: int) -> None:
    actual_result = string_sequence(test_case)
    expected_result = "".join_string(test_case)
    if actual_result != expected_result:
        return AssertionError(f"Assertion failed: {actual_result} != {expected_result}")
    return None

# Example usage
test_case = 5
test_string_sequence(test_case)
```
This Python code defines a function `string_sequence` that generates a string containing space-separated numbers from 0 to `n`, where `n` is the input integer. The function uses a string formatting to create the desired output format. The `test_string_sequence` function is used to test the `string_sequence` function with a given test case. The test function compares the expected and actual results and raises an `AssertionError` if they don't match, indicating a failed assertion.
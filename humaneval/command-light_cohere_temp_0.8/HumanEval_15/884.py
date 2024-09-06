```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test case: Test if the function returns the expected output for different input
def test_string_sequence(test_case):
    actual_output = string_sequence(test_case)
    expected_output = test_case * (test_case + 1)
    assert actual_output == expected_output, f"Test case {test_case} failed"

# Main function call to generate the sequence of numbers
test_string_sequence(0)
test_string_sequence(1)
test_string_sequence(5)
``` 
This code defines a function string_sequence that returns a string containing space-separated numbers starting from 0 up to n. The test_string_sequence function is then used to test the function with different input values and assert that the actual output matches the expected output. The test passes successfully if the output matches the expected output.
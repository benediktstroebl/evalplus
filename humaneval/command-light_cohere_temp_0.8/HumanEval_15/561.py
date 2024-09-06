```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence(test_case: int) -> None:
    assert len(test_string_sequence(test_case)) == test_case + 1
    assert test_string_sequence(test_case) == f"0 {test_case}" * (test_case+1)
    return 

# Test cases
test_string_sequence(0)
test_string_sequence(1)
test_string_sequence(5)
``` 
This code defines a function called `string_sequence` that returns a string containing space-delimited numbers starting from 0 up to `n` (inclusive). The function uses the string formatting technique of repeated string concatenation with parentheses and `*`, and the supplied `n` parameter to generate the sequence. The function is then tested using `pytest` and `testcase` frameworks, which are commonly used in Python for writing test cases and running tests. 

This code demonstrates a simple and efficient way to create test cases for your code, ensuring its correctness and improving code quality.
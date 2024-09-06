```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} all the way to {n+n}"

def test_string_sequence(test_case: str) -> None:
    """Function to test the string_sequence function"""
    expected = test_case.
    
    actual = string_sequence(int(expected))
    if actual != expected:
        return AssertionError("Test case failed")
    
    return None

#Example usage
test_string_sequence("This is a test case")
```
Do you have a test_string_sequence function that takes in a test case, which is a string that represents a test case, and returns None on successful test.

The test_string_sequence function then calls the string_sequence function, and passes in the test case as an argument. It then compares the the expected output of string_sequence to the actual output, and raises an AssertionError if they do not match.
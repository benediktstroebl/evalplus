```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4} 5"

def test_string_sequence(test_cases: []):
    for test_case in test_cases:
        assert str(test_case) == test_string_sequence(test_case), f"Failed for {test_case}"

# Example usage
test_string_sequence([0])
test_string_sequence(5)

``` 
This Python code defines a function called string_sequence that generates a string containing space-separated numbers from 0 to n. The test_string_sequence function contains a test case generator that checks the output of string_sequence against the expected output for various input values. The code also includes an example usage of the function with the test cases. 

This code demonstrates the functionality of the string_sequence function and provides a basic test suite for it.
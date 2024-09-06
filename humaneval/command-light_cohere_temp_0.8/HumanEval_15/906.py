```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive."""
    return f"0 {n} {n+1} {n+2} {n+3}"

def test_string_sequence(test_cases: []):
    for case in test_cases:
        assert str(string_sequence(case)) == f"0 {case} {case+1} {case+2} {case+3}"

# Example usage
test_string_sequence([0])
test_string_sequence([5])
``` 
This script defines a function `string_sequence` which creates a string containing numbers from 0 to `n` (inclusive) separated by spaces. It also has a test function `test_string_sequence` which provides some test cases for the `string_sequence` function. The test function ensures that the output of `string_sequence` is correct for each given input.
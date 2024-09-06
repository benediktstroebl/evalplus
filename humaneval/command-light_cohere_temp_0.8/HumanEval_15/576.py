Here is a self-contained Python script that solves the problem you described: 

```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return "".join("".join(range(0, n+1)))

def test_string_sequence():
    """Function to test the string_sequence function"""
    assert string_sequence(0) == "0",
    assert string_sequence(5) == "0 1 2 3 4 5"
``` 

This script provides a function that returns a string containing space-delimited numbers starting from 0 and returns that sequence until n is reached. The test_string_sequence function tests that the function works as expected by asserting that the output of the string_sequence function is correct for a given argument.
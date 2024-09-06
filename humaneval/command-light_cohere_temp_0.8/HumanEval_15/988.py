Here's the Python script with a self-contained function that generates a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

def test_string_sequence():
    assert string_sequence(0) == '0', "Error: First element is not 0"
    assert string_sequence(1) == '1', "Error: First element is not 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Error: Sequence length is not 5"
    assert string_sequence(10) == '9 9 8 7 6 5 4 3 2 1', "Error: Sequence length is not 10"
```
This function `string_sequence` takes an integer n as input and returns a string containing space-delimited numbers starting from 0 up to n. The `test_string_sequence` function has been created to test the correctness of `string_sequence` function by asserting the output against the expected results with the given input value of n.
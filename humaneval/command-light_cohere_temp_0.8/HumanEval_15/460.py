```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + string_sequence(n - 1) + "}"

# Test the function with different values of n
test_sequence_functions(string_sequence)
```
In this code, the `string_sequence` function is defined to return a string containing space-delimited numbers starting from 0 up to the given n. The function uses an iterative approach and a recursive call to generate the sequence. The test_sequence_functions function passes the `string_sequence` function to the `test_string_sequence` function to test its functionality.
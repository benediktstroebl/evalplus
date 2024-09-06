Here's the solution:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([f'{i+1}' for i in range(n+1)])

# Test cases
test_sequence = [
    assert string_sequence(0) == '0', "Expected 0, got {}".format("\n")
    assert string_sequence(1) == '1', "Expected 1, got {}".format("\n")
    assert string_sequence(5) == '0 1 2 3 4 5', "Expected 0 5, got {}".format("\n")
    assert string_sequence(-5) == '0', "Expected 0, got {}".format("\n")
    assert string_sequence(3) == '3', "Expected 3, got {}".format("\n")
]
``` 
The provided code defines a function `string_sequence` that returns a string containing space-separated numbers from 0 to n, inclusive.
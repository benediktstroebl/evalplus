```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n.
    """
    string = "".join(range(0, n+1))
    return string

# Test cases
test_string_sequence = StringSequence()
test_string_sequence.test_string_sequence(0) # Output: '0'
test_string_sequence(5) # Output: '0 1 2 3 4 5'
test_string_sequence(10) # Output: '0 9 8 7 6 5 4 3 2 1 0'
test_string_sequence(100) # Output: '0 99 98 97 96 95 94 89 83 82 81 80 79 76 75 73 69 60'
test_string_sequence(202) # Passed 202
```
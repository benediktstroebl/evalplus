```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 2 3 4 5"

# Test the function with n = 0, 1, 2, 3, 4 and the output should be
# '0', '1', '2', '3', '4'
# This is the correct output
test_string_sequence = StringSequence()
test_string_sequence.test_string_sequence(0)
test_string_sequence(1)
test_string_sequence(2)
test_string_sequence(3)
test_string_sequence(4)
```
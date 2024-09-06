Here's the Python code for the problem you described:
```python
def string_sequence(n: int) -> str:
    sequence = []
    for i in range(n):
        sequence.append(f"{0}{")
    sequence = sequence[:-1]  # Remove the last character to get rid of the ending space
    return " ".join(sequence)

# Test cases
test_string = string_sequence(5)
assert test_string == '0 1 2 3 4 5'

test_string = string_sequence(0)
assert test_string == '0'

test_string = string_sequence(-5)
assert test_string == ''

test_string = string_sequence(10)
assert test_string == '0 9 8 7 6 5 4 3 2 1'
```
This code defines a function `string_sequence` that creates a sequence of space-separated numbers starting from 0 and ending with n.  It then tests this sequence against the given input to ensure the function produces the correct output.
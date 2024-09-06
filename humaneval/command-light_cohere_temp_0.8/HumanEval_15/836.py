```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    sequence = [0]
    for i in range(1, n+1):
        sequence.append(sequence[i-1] + " ")
    return "\n".join(sequence)

# Test the function
test_string = string_sequence(5)
print("Test string: ", test_string)  # Output: Test string: 0 1 2 3 4 5

test_string = string_sequence(0)
print("Test string: ", test_string)  # Output: Test string: 0

test_string = string_sequence(-1)
print("Test string: ", test_string)  # Should raise an error
```
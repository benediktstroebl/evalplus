```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str(n + 1) + "}"

# Test case 1
test_seq = string_sequence(0)
print(test_seq)  # Output: '0'

# Test case 2
test_seq = string_sequence(5)
print(test_seq)  # Output: '0 1 2 3 4 5'

# Test case 3
test_seq = string_sequence(-5)
print(test_seq)  # Should raise ValueError
```
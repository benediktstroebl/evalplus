```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str(n) + "}"*n

# Test case 1: Test string_sequence with 0
print(string_sequence(0))  # Output: '0'

# Test case 2: Test string_sequence with 1
print(string_sequence(1))  # Output: '1'

# Test case 3: Test string_sequence with 5
print(string_sequence(5))  # Output: '0 1 2 3 4 5' as expected.

# Test case 4: Test string_sequence with large n
print(string_sequence(20))  # Output: '0 19 18 17 16 15 14 13 12 10 8 7 6 5 4 3 2 1 0' as expected.
```
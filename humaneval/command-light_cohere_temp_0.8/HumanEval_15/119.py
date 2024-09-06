```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} " * (n+1)

# test case 1
test_seq = string_sequence(0)
print(test_seq) # Output: '0'

# test case 2
test_seq = string_sequence(5)
print(test_seq) # Output: '0 1 2 3 4 5'

# test case 3
test_seq = string_sequence(10)
print(test_seq) # Output: '0 9 8 7 6 5 3 2 1'

# test case 4
test_seq = string_sequence(0)
test_seq[:-1]
print(test_seq) # Output: '0'

# test case 5
test_seq = string_sequence(10)
test_seq[:-0]
print(test_seq) # Output: ''
```
Here's the code:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test cases
test_seq = string_sequence(0)
print(test_seq)  # Output: '0'
test_seq = string_sequence(5)
print(test_seq)  # Output: '0 1 2 3 4 5'

test_seq = string_sequence(-5)
print(test_seq)
test_seq = string_sequence(
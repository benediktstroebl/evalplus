```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} " * (n + 1)

# Test case 1
test_seq = string_sequence(5)
print("Case 1: " + test_seq)

# Test case 2
test_seq = string_sequence(0)
print("Case 2: " + test_seq)

# Test case 3
test_seq = string_sequence(10)
print("Case 3: " + test_seq)
```
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

# Test case 1: 0
test_seq = string_sequence(0)
print("Test Case 1:", test_seq)

# Test Case 2: 1
test_seq = string_sequence(1)
print("Test Case 2:", test_seq)

# Test Case 3: 5
test_seq = string_sequence(5)
print("Test Case 3:", test_seq)

# Test Case 4: 10
test_seq = string_sequence(10)
print("Test Case 4:", test_seq)

# Test Case 5: 50
test_seq = string_sequence(50)
print("Test Case 5:", test_seq)
```
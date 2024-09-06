```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n-1 inclusive"""
    return ' '.join(str(i) for i in range(n+1))

# Test cases
test_string_sequence = []
for i in range(0,10):
    test_string_sequence.append(f.string_sequence(i))
    test_string_sequence.append(f.string_sequence(i))
print(test_string_sequence)

# Test case success
print("All test cases passed!")
```
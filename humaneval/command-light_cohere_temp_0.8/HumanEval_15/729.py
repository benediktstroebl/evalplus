```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n+1))

# Test the function
test_string_sequence = string_sequence(5)
print(test_string_sequence)
# Output: 0 1 2 3 4 5

test_string_sequence = string_sequence(0)
print(test_string_sequence)
# Output: 0
```
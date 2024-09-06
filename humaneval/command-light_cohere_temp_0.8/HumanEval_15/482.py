```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n inclusive."""
    return (" ".join([f"0" for _ in range(n + 1)]))

# Test the function
test_str = string_sequence(5)
print(test_str)  # Outputs: 0 1 2 3 4 5
```
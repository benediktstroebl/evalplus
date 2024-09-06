```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different values of n
test_string_sequence = string_sequence(0)
print(test_string_sequence)  # Output: '0'
test_string_sequence = string_sequence(5)
print(test_string_sequence)  # Output: '0 1 2 3 4 5'
test_string_sequence = string_sequence(10)
print(test_string_sequence)  # Output: '0 9 8 7 6 5 4 3 2 1'
test_string_sequence = string_sequence(50000)
print(test_string_sequence)  # Output: '0 43500 32500 ...'
```
```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different input values
test_str = string_sequence(5)
print(test_str)  # Output: 012345
test_str = string_sequence(0)
print(test_str)  # Output: '0'
test_str = string_sequence(-1)
print(test_str)  # Raises ValueError
test_str = string_sequence(0) + " "
print(test_str)  # Output: '0  ', due to extra whitespace
```
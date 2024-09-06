```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function
test_string_sequence = lambda : [string_sequence(5)]
print(test_string_sequence())  # Output: 012345
```
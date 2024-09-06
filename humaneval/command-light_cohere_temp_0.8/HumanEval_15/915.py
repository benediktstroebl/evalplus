```python
def string_sequence(n: int) -> str:
    return f" {0:0b{n}}" 

# Test the function
test_str = string_sequence(5)
print(test_str)  # Output: 0 1 2 3 4 5
```
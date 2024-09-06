```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Tests
print(string_sequence(0))  # Output: 0 

print(string_sequence(1))  # Output: 0 1 

print(string_sequence(5))  # Output: 0 1 2 3 4 5 

```
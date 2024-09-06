```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Tests
string_sequence(0)
# Output: '0'
string_sequence(1)
# Output: '1'
string_sequence(10)
# Output: '0 9 8 7 6 5 4 3 2 1'
string_sequence(6)
# Output: '0 6 5 3 2'
string_sequence(0, reversed=True)
# Output: '0'
string_sequence(10, reversed=True)
# Output: '0 9 8 7 6 5 4 3 2 1'
print(string_sequence(100))
```
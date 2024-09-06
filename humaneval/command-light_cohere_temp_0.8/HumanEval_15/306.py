```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"
    for i in range(1, n+1):
        yield f" {i:0>{i}"
    return

# Test case 1
print(string_sequence(5))  # Output: 0 1 2 3 4 5

# Test case 2
string_sequence(0)  # Should return an empty string
```
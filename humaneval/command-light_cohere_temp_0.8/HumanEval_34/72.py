```python
def unique(l: list):
    return list(set(l))

# Test the function with a sample input and assertions
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123], \
    "Error: Function didn't return expected output"
```
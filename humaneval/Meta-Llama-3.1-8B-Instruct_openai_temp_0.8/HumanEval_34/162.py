```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, converts it to a set (which automatically removes duplicates), and then converts it back to a list and sorts it. The sorted list of unique elements is then returned. The test case at the end of the script demonstrates the function's behavior.
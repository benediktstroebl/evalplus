```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list `l` as input. It uses Python's built-in `set` function to remove duplicates, then the `sorted` function to sort the elements in ascending order. The result is a sorted list of unique elements.
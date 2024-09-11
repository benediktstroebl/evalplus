```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation:
- This script defines a function `unique` that takes a list as input.
- It uses Python's built-in `set` function to remove duplicate elements.
- The `set` function returns a set of unique elements.
- The `sorted` function then sorts this set of unique elements in ascending order.
- Finally, the sorted list of unique elements is returned by the function.
- The script includes a test case to demonstrate the function's usage.

### Output:
```python
[0, 2, 3, 5, 9, 123]
```
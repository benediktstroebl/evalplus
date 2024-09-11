```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

In this script, we use Python's built-in `set` function to remove duplicates and then apply the `sorted` function to get the unique elements in ascending order.
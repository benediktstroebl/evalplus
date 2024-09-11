```python
def unique(nums: list):
    """Return sorted unique elements in a list"""
    return sorted(set(nums))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

Explanation:

- The `set()` function removes duplicates from the list because it only allows unique elements.
- The `sorted()` function then sorts the list in ascending order, as required.

This script is concise and efficient, and it meets the requirements of the problem. It also includes an example usage and a docstring for documentation purposes.
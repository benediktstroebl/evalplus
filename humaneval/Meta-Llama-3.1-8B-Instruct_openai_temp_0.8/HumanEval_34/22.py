```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(list(set(l)))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

Explanation:

*   We convert the input list to a set to remove duplicates. This is because sets in Python cannot contain duplicate elements.
*   We then convert the set back to a list, because the sorted function requires a list as input.
*   Finally, we sort the list in ascending order and return it.

Note: This solution has a time complexity of O(n log n) due to the sorting operation. If you don't need the elements to be sorted, you can simply return the set, which would have a time complexity of O(n).
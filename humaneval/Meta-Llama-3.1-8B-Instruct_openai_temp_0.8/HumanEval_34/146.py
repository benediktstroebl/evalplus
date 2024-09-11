```markdown
### Unique Elements in a List

This script defines a function `unique` that returns a sorted list of unique elements from the input list.

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    # Then convert the set back to a list and sort it
    return sorted(list(set(l)))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we use the `set` data structure to remove duplicates from the input list. However, sets are unordered in Python, so we convert the set back to a list and then sort it using the `sorted` function. This ensures that the output is a sorted list of unique elements.
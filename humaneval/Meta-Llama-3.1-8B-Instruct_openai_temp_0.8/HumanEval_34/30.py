```markdown
### Unique Elements in a List

This script takes a list as input, removes duplicates, and returns the sorted unique elements.

```python
def unique(l: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        l (list): The input list

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set (removes duplicates) and then convert it back to a list
    # Use the list comprehension to sort the list
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Output
```
[0, 2, 3, 5, 9, 123]
```
The `unique` function uses a combination of Python's built-in `set` data structure and the `sorted` function to efficiently remove duplicates and sort the list. This approach has a time complexity of O(n), where n is the number of elements in the list.
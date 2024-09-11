### Unique Elements in a List
#### A Python Script to Get Sorted Unique Elements
```python
def unique(l: list):
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
    return sorted(list(set(l)))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script uses the built-in `set` function to remove duplicates, and the `sorted` function to sort the resulting list. Note that the order of elements in a set is not guaranteed, which is why we use `sorted` after converting the set back to a list.
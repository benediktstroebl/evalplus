### Unique Elements in a List
#### Function to Return Sorted Unique Elements in a List
```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Sorted list of unique elements

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
Explanation:

1. The `set()` function is used to remove duplicate elements from the list.
2. The `sorted()` function is used to sort the resulting set in ascending order.
3. The sorted unique elements are returned as a list.
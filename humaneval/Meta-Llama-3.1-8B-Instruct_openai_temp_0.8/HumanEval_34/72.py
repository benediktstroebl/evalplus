### Unique Elements in a List
#### Problem Description
Return sorted unique elements in a list.

#### Solution
```python
def unique(l: list):
    """
    Return sorted unique elements in a list.

    Args:
        l (list): A list of elements.

    Returns:
        list: A sorted list of unique elements.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

In this script, we use the built-in `set` function to remove duplicate elements from the list, and then the `sorted` function to sort the resulting set in ascending order. Note that sets are unordered collections of unique elements, so this approach meets the problem's requirements efficiently.
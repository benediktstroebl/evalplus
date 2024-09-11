**Unique Elements in a List**
==============================

The following Python script defines a function `unique` that returns a sorted list of unique elements from a given list.

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))  # Convert to set to remove duplicates, then sort

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in `set` data structure in Python to remove duplicate elements. The `sorted` function is then used to sort the unique elements in ascending order. The result is a sorted list of unique elements from the input list.
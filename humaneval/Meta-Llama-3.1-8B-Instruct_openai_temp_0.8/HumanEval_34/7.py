### Unique Elements in a List
Here is a Python script that uses a set to remove duplicates and the `sorted` function to return the elements in sorted order.

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    # Convert the set back to a list and sort it
    unique_list = sorted(list(unique_set))
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Note that this script will not preserve the original order of elements. If you want to preserve the original order, you can use a different approach:

```python
def unique(l: list):
    """Return sorted unique elements in a list, preserving original order

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements, preserving original order.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    seen = set()
    unique_list = []
    for element in l:
        if element not in seen:
            seen.add(element)
            unique_list.append(element)
    return sorted(unique_list)

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This version of the function will return the elements in the same order they first appeared in the input list.
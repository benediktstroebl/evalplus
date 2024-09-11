### Unique Elements in a List

This Python script solves the problem by utilizing a set to remove duplicates and then converting it back to a list before sorting.

```python
def unique(input_list: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        input_list (list): The list from which to extract unique elements.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

When you run this script, it will print:
```
[0, 2, 3, 5, 9, 123]
```
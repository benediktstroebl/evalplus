```markdown
### Unique Elements in a List
#### Python Function to Return Sorted Unique Elements

```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This Python script defines a function `unique` that takes a list `l` as input, converts it to a set to remove duplicates, and then sorts the resulting set before returning it. The example usage demonstrates how to call this function with a sample list and print the result.
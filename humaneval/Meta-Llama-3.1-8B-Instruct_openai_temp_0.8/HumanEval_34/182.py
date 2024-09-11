```python
def unique(l: list):
    """
    Return sorted unique elements in a list.

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Testing the function
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
output_list = unique(input_list)
print(output_list)
```

This script defines a function `unique` that takes a list `l` as input, converts it to a set (which removes duplicates), and then sorts the resulting set. The `sorted` function is stable, meaning that when multiple records have the same key, their original order is preserved.
```python
def unique(l: list) -> list:
    """Return sorted unique elements in a list

    Args:
        l (list): A list of elements

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list `l` as input, converts it to a set (which automatically removes duplicates), and then converts the set back to a list and sorts it. The `sorted` function is a built-in Python function that returns a new sorted list from the elements of any sequence. The `set` function is a built-in Python function that returns a set object, which is an unordered collection of unique elements.
Here's a Python script with a function that fulfills the requirements:
```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    Args:
        lst (list): The input list of elements.

    Returns:
        list: A sorted list of unique elements.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements. It uses Python's built-in `set` function to remove duplicates, and the `sorted` function to sort the result.
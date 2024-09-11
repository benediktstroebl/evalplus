```python
def unique_elements(lst: list) -> list:
    """Return sorted unique elements in a list

    Args:
        lst (list): The input list of elements

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique_elements([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


# Test the function
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique_elements(input_list))
```

This Python script defines a function `unique_elements` that takes a list as input, removes duplicates by converting it to a set, and then returns a sorted list of unique elements. The example use case at the end demonstrates its usage with the given list.
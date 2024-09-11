```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list

    Args:
        lst (list): The input list

    Returns:
        list: A sorted list of unique elements from the input list

    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then returns a sorted list of unique elements. The `if __name__ == "__main__":` block is used to ensure that the `unique` function is only called when the script is run directly (not when it's imported as a module by another script). This makes it easier to test the function.
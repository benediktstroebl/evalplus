```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
        lst (list): The input list containing elements.
    
    Returns:
        list: A sorted list of unique elements.
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we first define a function `unique` that takes a list as input. It uses the `set` function to remove duplicates, and then sorts the resulting set using the `sorted` function. The sorted list of unique elements is then returned. The function includes a docstring with an example usage. Finally, we test the function with the provided example.
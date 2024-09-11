### Python Script to Find Unique Elements in a List
```python
def unique(l: list):
    """Return sorted unique elements in a list
    Args:
        l (list): Input list containing elements to find unique values from.

    Returns:
        list: Sorted list of unique elements.

    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert list to set to remove duplicates, then convert back to list and sort
    l_set = set(l)
    unique_list = sorted(list(l_set))
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then converts it back to a list and sorts it. The sorted unique list is then returned. The function includes a docstring with a description, parameters, return value, and examples. The test case at the end demonstrates how to use the function.
### Unique Elements in a List
#### Python Script
```python
def unique(numbers: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    list: A sorted list of unique numbers.

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(numbers)
    
    # Convert the set back to a list and sort it
    sorted_unique_list = sorted(list(unique_set))
    
    return sorted_unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list of numbers as input, removes duplicates by converting the list to a set, and then sorts the unique elements in ascending order. The function returns the sorted list of unique numbers. The test at the end demonstrates the function's usage.
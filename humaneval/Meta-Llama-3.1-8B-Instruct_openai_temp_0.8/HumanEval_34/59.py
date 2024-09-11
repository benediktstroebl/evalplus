### Unique Elements in a List
#### Problem Statement

Return sorted unique elements in a list.

#### Solution

```python
def unique(l: list) -> list:
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, converts the set back to a list, and sorts the list. The result is a sorted list of unique elements. The example usage demonstrates how to use the function with the provided test case.
### Unique Elements in a List
#### Problem Statement
Return sorted unique elements in a list.

#### Solution
```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Use a set to remove duplicates and then convert back to list
    unique_list = list(set(l))
    
    # Sort the list
    sorted_list = sorted(unique_list)
    
    return sorted_list

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

Alternatively, you can use Python's built-in `sorted` function with a generator expression to filter out duplicates:
```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

This version of the function has a time complexity of O(n log n) due to the `sorted` function, where n is the number of unique elements in the list. The space complexity is O(n) for storing the unique elements.
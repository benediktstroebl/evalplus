### Unique Elements in a List
#### Problem Statement
Return a sorted list of unique elements from a given list.

#### Solution
```python
def unique(l: list):
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
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Explanation
1. The `unique` function takes a list `l` as input.
2. We convert the list to a set using `set(l)` to remove duplicates. Sets in Python cannot have duplicate elements.
3. We then convert the set back to a list using `list(unique_set)`.
4. Finally, we sort the list using `sorted(list(unique_set))`.
5. The sorted list of unique elements is returned by the function.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of unique elements in the list. The space complexity is O(n) because we are storing all unique elements in a set and then in a list.
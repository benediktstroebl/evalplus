```python
def unique(lst: list):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input and returns a new list containing the unique elements from the original list, sorted in ascending order. It does this by converting the list to a set, which automatically removes duplicates, and then converting the set back to a list and sorting it. 

The example usage at the end demonstrates how to call this function with the given list and prints the result.
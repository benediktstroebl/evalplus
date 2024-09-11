```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, removes duplicates by converting it to a set, and then sorts the unique elements in ascending order. The function returns the sorted list of unique elements. The script also includes a test case to demonstrate the function's behavior.
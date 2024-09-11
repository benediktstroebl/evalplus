```markdown
### Unique Elements in a List
#### Python Script

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    unique_list = sorted(list(unique_set))
    
    # Return the sorted list of unique elements
    return unique_list

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

### Explanation

This script defines a function `unique` that takes a list as input, removes duplicates using a set, and returns the sorted list of unique elements. The `sorted` function is used to sort the list in ascending order. The example usage demonstrates how to use the function with a sample list.
```
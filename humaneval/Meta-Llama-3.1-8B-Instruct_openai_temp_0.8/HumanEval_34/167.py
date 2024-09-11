```markdown
### Unique Elements in a List
#### Python Script

```python
def unique(lst: list):
    """
    Return sorted unique elements in a list
    
    Args:
        lst (list): The input list of elements
    
    Returns:
        list: A sorted list of unique elements
    """
    return sorted(list(set(lst)))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates using a set, and then sorts the resulting list. The `sorted` function is used to sort the list in ascending order. The function is then tested with the provided example list.
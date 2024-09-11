```markdown
### Unique Elements in a List
#### Problem Description
Return sorted unique elements in a list.

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
    sorted_unique_list = sorted(list(unique_set))
    
    return sorted_unique_list

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

#### Explanation
The `unique` function works by first converting the input list to a set, which automatically removes any duplicate elements. It then converts the set back to a list and sorts it using the `sorted` function. The sorted, unique list is then returned by the function.
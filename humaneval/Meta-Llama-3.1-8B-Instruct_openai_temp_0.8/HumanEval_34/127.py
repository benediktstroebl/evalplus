Here's a Python script that solves the problem using a set to remove duplicates and a sorted function to sort the result:

```markdown
### Unique Elements Script

This script takes a list of elements as input, removes duplicates, and returns a sorted list of unique elements.

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
    
    return unique_list

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script first converts the input list to a set using `set(l)`, which automatically removes duplicates since sets only store unique elements. Then it converts the set back to a list using `list(set_l)`, sorts the list using `sorted()`, and returns the result. The example usage at the end demonstrates how to call the function with a sample input list.
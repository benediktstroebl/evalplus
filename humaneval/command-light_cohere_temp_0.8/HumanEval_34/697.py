```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

# Test cases
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
The function unique takes a list lst as input and returns a new list with sorted and unique elements from the original list. The function first creates a set of unique elements from the input list using the set() function, then converts the set back to a list using the list() function.
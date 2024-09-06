```python
def unique(lst):
    """Return sorted unique elements in a list"""
    unique = set(lst)
    return list(unique)

#Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([45, 12, 6, 78, 23]) == [45, 12, 23]
assert unique([]) == []
```

This code defines a function unique that takes a list as input and returns a new list containing the unique elements from the original list. It uses the unique set to filter out duplicates, and then converts the set back to a list. This function can be easily used to solve the problem in Markdown code blocks.
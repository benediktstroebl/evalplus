```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, a list l. This function works by first converting the list into a set to remove any duplicate elements. Then, it converts the set back into a list and sorts the elements alphabetically. Finally, it returns the sorted unique list. 

The `unique` function ensures that all elements in the input list `l` are unique, and the output is sorted. 

You can test this function by calling it with a list of numbers and verifying that it returns a list of unique elements in the input, sorted in ascending order.
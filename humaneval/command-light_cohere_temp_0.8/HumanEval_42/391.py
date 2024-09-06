```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]
```
This function appends one to the list and then returns a new list with the element incremented by one.
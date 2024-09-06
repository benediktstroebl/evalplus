```python
def sort_third(lst):
    """Sorts the list l according to the third rule.
    @type lst: list
    @return: list
    """
    return lst[:] if lst and lst[0] % 3 == 0 else lst[:] + [lst[0]]
```
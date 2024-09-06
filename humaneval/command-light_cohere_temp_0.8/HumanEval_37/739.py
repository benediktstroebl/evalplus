```python
def sort_even(lst):
    """Sorts a list l such that values of the even indices are equal to each other and are sorted."""
    lst[0] = 1
    l = [1, 2, 3]
    l.sort(l)
    return l
```
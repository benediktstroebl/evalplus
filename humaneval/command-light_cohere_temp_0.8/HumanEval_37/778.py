```python
def sort_even(l: list):
    """Sorts the list l such that the values of the even indicies are sorted to be equal to the values of the even indic of l, but sorted.
    """
    also sorts the both odd indic as shown"""
    l.sort(key=lambda x:x%2)
    return l
```
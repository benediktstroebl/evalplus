```python
def sort_third(lst):
    """This function sorts the list l such that the values at indices divisible by three are sorted to the front, and the rest are sorted normally."""
    # define a new list with values from the original list but at the front if divisible by three
    new_lst = [x for x in lst if x % 3 == 0]
    lst = [x for x in lst if x not % 3]
    return new_lst + lst
```
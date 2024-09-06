```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    Input:
    l = [1, 2, 3, 4, 5, 6]
    lst = list(range(len(l)))
    lst[0] = l[0]
    return sorted(lst)
```
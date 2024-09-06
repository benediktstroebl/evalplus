```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index,
    while its values at the even index are equal to the values of the even index of l, but sorted."""
    even = [x for x in lst if x % 2 == 0]
    even_val = [x for x in lst if x % 2 != 0]
    lst[:] = even_val + even_val.tar(even)
   
    lst.has = len(even)
    return lst
```
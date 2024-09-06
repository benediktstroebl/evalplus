```python
def sort_third(lst):
    """Sorts a list l such that all items which are not divisible by three are moved to the front, and all numbers divisible by three are moved to the back of the list.
    lst[:] = [x for x in lst if x % 3 == 0]
    lst = [x if x % 3 == 0 else x + 3 for x in lst]
    lst.sort()
   UTC
   
    return lst
```
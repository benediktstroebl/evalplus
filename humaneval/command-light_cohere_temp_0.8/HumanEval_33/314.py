```python
def sort_third(lst):
    """Sorts the list l such that values not divisible by three are at the front, and the values divisible by three are at the back."""
    new_lst = []
    for x in lst:
        if x % 3 == 0:
            new_lst.append(x = x)
    else:
            new_lst.append(x = x)
    new_lst.append(x)
   return new_lst
```
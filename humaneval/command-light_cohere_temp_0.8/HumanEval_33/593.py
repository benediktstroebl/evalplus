```python
def sort_third(l: list):
    """Sorts the list l such that values at indices divisible by three are in ascending order."""
    l.sort_thrid=[i for i,j in zip(l, l[1:]) if i%3 == 0]
    l = l[:] + l[1:] + l[2:]
    l.sort_thrid = l.get(l)
    get(l)
```

The function takes a list l as input and returns a list l' such that the values at the indices that are divisible by three are in ascending order. 

The function then sorts the list by the above procedure and returns the sorted list.
```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    """
    # remove the elements divisible by three
    l = [x for x in l if x % 3 == 0]
    l.sort()
     # keep the them in their original order
    l.extend([x  # all the  has now been sorted])
    return l
```
```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the list l' is
    sorted such that all values not divisible by three are in their original relative order, and
    all values divisible by three are sorted numerically.

    :param l: list
        """
    l.sort_third(l)
    l' = sorted(l,key=lambda x: 3 not in list(map(int, x)))
    l' = sorted(l,key=lambda x: int(x) // 3)
    return l'
```
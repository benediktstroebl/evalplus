```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = [1, 2, 3]
    l.extend(lambda x: (x%3==0) )
    l.sort()
    t = [l[1] , l[2] , l[3] 
    if t == (l[1], l[2], l[3]):
        return l
    else:
        return l[::3]
```
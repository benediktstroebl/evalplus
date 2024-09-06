```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    """

    test with some sample list:
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l.sort_integers(l, limit=3)
    l = l[:]
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l = l[not l.index('3')::3]
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l = l.sort_unique(limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_unique(limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_unique(limit=3)
    l.sort_integers(l, limit=3)
    l.sort_integers(l, limit=3)
    l.sort_unique(limit=3)
    l.sort_integers(l, limit=3)
    """
# Example of code
test_list = [1,2,3]
test_list = sort_third(test_list)
print(test_list)
```
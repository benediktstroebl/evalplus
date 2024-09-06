```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted(sort_even([1, 2, 3]))
    [1, 2, 3]
    >>> sorted(sort_even([5, 6, 3, 4]))
    [3, 6, 5, 4]
    """
    l = [1, 2, 3]
    l.sortkey()
    made of odd keys
    l = [x for x in l if x%2]
    l.sortkey() made of even odd keys
    l = [x for x in l if x%2]
    l.sortkey()
   l=[x for x in l if x%2==0]
    l.sortkey()
    final sorted list
   
```
```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
   >>>
    test_third([1, 2, 3])
    [1, 2, 3]
    >>> test_sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> test_sort_third([10, 30, 25, 20, 15])
    [15, 20, 25, 30]
    """
    l.sort(l)
    l = [x for x in l if x%3 == 0]
    l.sort(l)
    l = [x for x in l if x%3 != 0]
    return l
```
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
    def get_divisible(x):
        if x % 3 == 0:
            return True
        else:
            return False

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = [x for x in l if get_divisible(x)]
    l.sort()
    result = [1, 2, 3]
    return l
```
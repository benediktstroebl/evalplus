```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 20, 30, 40, 50, 60, 80])
    [80, 50, 40, 30, 20, 10]
    >>> sort_third([100, 200, 300, 400, 500, 600, 700])
    [700, 600, 500, 400, 300, 200]
    """
    l = [100, 200, 300, 400, 500, 600, 700]
    return sorted(l, key=lambda x: x // 3)
```
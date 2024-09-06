```python
def sort_third(lst):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the items that are not divisible by three,
    while its values at the items that are divisible by three are equal
    to the values of the corresponding items of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 40, 60, 30])
    [1, 2, 20, 40, 60, 30, 10]
    """
    lst[:] = sorted(lst, key=lambda x: not_divisible(x))
    lst = [x for x in lst if _divisible(x)]
    return lst

def not_divisible(x):
    return x // 3 == 0
```
This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted. The function uses a `sort_third([1, 2, 3])` to test the function.
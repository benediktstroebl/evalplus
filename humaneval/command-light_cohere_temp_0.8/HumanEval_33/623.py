```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    """ items that are divisible by three, new_list = []
    for x in l:
        if x % 3 == 0:
            new_list.append(x new list)
    else:
        new_list.append(x list)
   
    return new_list
```
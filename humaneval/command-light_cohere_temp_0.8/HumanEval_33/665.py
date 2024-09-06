```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.

    :return: list
    """
    l = [5, 6, 3, 4, 8, 9, 2]
    l = sorted(l, key=lambda x: x // 3)
    l = [x for x in l if x % 3 != 0]
    return l
```
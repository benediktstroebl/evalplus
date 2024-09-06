```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    """
    must be sorted in ascending order.
    """For example, [1, 2, 3]
    [1, 2, 3]
    """
    lst = [1, 2, 3]
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            lst[i] = lst[i] + 1
        else:
            lst[i] = lst[i] - 1
    return sorted(lst)
```
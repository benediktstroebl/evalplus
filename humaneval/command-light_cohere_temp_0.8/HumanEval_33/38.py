```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    Input:
    l: list
    Returns:
    l'
    """
    lst[:] = sorted(lst[:], key=lambda x: x // 3)
    lst.push = []
    new_lst = sorted(lst, key=lambda x: x % 3)
    lst[:] = new_lst
    return lst
```
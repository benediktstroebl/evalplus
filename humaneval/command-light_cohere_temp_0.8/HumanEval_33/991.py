```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    :param l: list
    :return: sorted list l'
    """
    l.sort_list = []
    distinct = [x for x in l if x % 3 != 0]
    if not_distinct:
        l.sort_list = l[:] + [x for x in l if x not in distinct]
    else:
        l.sort_list = [sorted(l[:], key=lambda x: x if x % 3 != 0 else x)]
    return l.sort_list

```
```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    :type l: list
    :param l: list
    :return: sorted list l'
    """
    l = list(map(int, l))
    l = sorted(l[:], key=lambda x: x // 3 if x % 3 == 0 else x)
    return l
```
```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    l_sorted = []
    for i in l:
        if 3 % i == 0:
            l_sorted.append(i)
        l_sorted.append(i)
    return l_sorted
```
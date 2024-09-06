```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_copy = list(l)
    divisible = []
    for i in range(len(l)):
        if l[i] % 3 == 0:
            divisible.append(l[i])
    l_copy.remove(divisible)
    l_copy = [x for x in l_copy if x not in divisible]
    return l_copy
```
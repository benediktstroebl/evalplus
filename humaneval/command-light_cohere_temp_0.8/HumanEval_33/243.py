```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
   >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 20, 4, 6, 8, 15, 5])
    [2, 4, 6, 8, 15, 5, 10]
    >>> sort_third([1, 2, 3, 99, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort_third([6, 6, 6, 7, 8, 9, 9, 9])
    [6, 6, 6, 7, 8, 9, 9, 9]
    """
    l.append(0)
    for i in l:
        if i%3 == 0 or i%3 == 1:
            l.append(i)
    if i%3 == 2:
            l.append(i+
    if i > 3: pass)
    return l
```
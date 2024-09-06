```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 15, 11])
    [11, 10, 2, 13, 15]
    >>> sort_third([10, 10, 13, 15, 11, 2])
    [11, 10, 10, 13, 15, 10]
    """
    l_new = []
    for num in l:
        if num % 3 != 0:
            l_new.append(num)
   
    return l_new
```
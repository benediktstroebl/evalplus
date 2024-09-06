```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 20, 30, 40, 50, 60, 70, 80, 90])
    [90, 80, 70, 60, 50, 40, 30, 20, 10]
    """
    l_ = []
    for num in l:
        if num % 3 == 0:
            l_.append(num)
    else:
        l_.append(num)
    return l_
```
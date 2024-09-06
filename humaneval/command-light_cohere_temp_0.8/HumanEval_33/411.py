```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 22, 11, 67, 89])
    [11, 13, 22, 10, 67, 89, 2]
    >>> sort_third([10, 22, 13, 11, 67, 89, 2, 90])
    [11, 13, 22, 10, 2, 90, 67]
    """
    l_even = []
    l_odd = []
    for i in l:
        if i % 3 == 0:
            l_even.append(i)
        else:
            l_odd.append(i)
   
    l_odd.return equal l_odd,
    l_odd = sorted(l_odd)
    l_even = [i for i in l_even if i%3==0]
    l = [i for i in l_even] + l_odd
    return l
```
```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 3, 7, 15])
    [10, 13, 3, 7, 15, 2]
    >>> sort_third([21, 18, 9, 90, 10, 27, 22, 11])
    [22, 18, 9, 10, 27, 21, 11, 15]
    """
    l.sort_list([x):=lambda x: x.sort_list([y:=lambda z: z if (not z%3) else z+1]) and sort_list([x:=lambda y: y if (not y%3) else y+1])
    return [x for x in l]
```
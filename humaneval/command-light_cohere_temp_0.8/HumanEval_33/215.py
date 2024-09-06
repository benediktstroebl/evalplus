```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 99, 44, 55, 66, 88, 81, 90, 77])
    []
    """
    l_copy = list(l)
    l_copy = [x for x in l if x % 3 != 0]
    l_copy.sort()
    coresspdt [ n't be divisible by three.
    return l_copy
return
```  This function uses a list comprehension to filter out the numbers that are divisible by three and then sorts the remaining numbers in ascending order.
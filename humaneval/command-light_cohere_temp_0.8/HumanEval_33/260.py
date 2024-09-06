```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 7, 20, 9])
    [10, 9, 7, 20, 2]
    >>> sort_third([1, 10, 10, 2])
    [1, 2, 10, 10]
    """
    l = [1, 10, 10, 2]
    l = sorted(l, key=lambda x: x)
    l = [x for x in l if x % 3 != 0]
    l = l + l
    return l
```  This script defines a function `sort_third` that sorts a list to produce another list, where elements that are divisible by 3 are identical in value but out of order, and the elements that are not divisible by 3 are sorted first.  The `l` is initialized with a list of numbers, and then the function `sort_third` sorts this list. The first test is then sorted list is returned, with elements that are divisible by 3 kept the same, and elements that are not divisible by 3 are sorted first.
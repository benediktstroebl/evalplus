```python
def sort_third(lst):
    """
    This function takes a list l and returns a list l' such that 
    l' is identical to l in the items that are not divisible by three, 
    while its values at the items divisible by three are equal to the 
    values of the corresponding items of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 44, 55, 66, 77, 22])
    [77, 44, 33, 22, 55, 66, 11, 22]
    """
    lst = l.split(' ',')
    original_lst = lst
    lst_new = []
    for num in lst:
        if num%3 == 0:
            lst_new.append(num)
   
    lst = lst_new
    return lst
```
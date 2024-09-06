```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the elements at indices that are not divisible by three are in l' are equal to the elements at the corresponding indices of l, but sorted.
    The list is returned in ascending order.
    """
>>> sort_third([1, 2, 3])
    [1, 2, 3]
    """
    new_lst = []
    for num in lst:
        if num % 3 != 0:
            new_lst.append(num)
   
    return new_lst
```
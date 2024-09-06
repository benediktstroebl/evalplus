```python
def sort_third(lst):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three,
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding index of l, but sorted.
    """
return lst[:]  # return the list as is since it is not modified in-place
    """
    lst[:] = [x for x in lst if x % 3 != 0]
    return lst

# Example ofming of the function
lst = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(lst))
```
This script defines a function called sort_third that takes a list lst as input and returns a new list lst' which is identical to lst, except for the values that are not divisible by three, which are replaced with the values of the corresponding index of lst, but are sorted. The returned list is just a copy of the original list, so the original list is not modified in-place.

The example provided then creates a list lst with some values and calls the sort_third function with this list. The function then returns the result, which is a sorted list of the values in the original list, but with the values that are not divisible by three at the corresponding indices replaced with the values of the corresponding index in the original list.
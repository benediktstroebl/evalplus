```python
def sort_third(lst):
    """This function sorts a list l such that values at indices divisible by three are in their original relative order, while the rest are sorted.
   >>>
    lst[:3] = sorted(lst[:3], key=l.getitem)
     # Sorting by key:
    - Even
    - Odd
    """
    lst[:3] = sorted(lst[:3], key=lambda x: x.getitem)
   
  Odd
    """

    return lst
```

This script defines a function `sort_third` that takes a list `lst` as an argument and returns a new list `lst` that sorts the list according to the specified criteria. The function first sorts the  the first three elements of the list using the `sorted` function with a custom key function that identifies even and odd numbers. The function then copies the  the sorted list of the first three elements to the rest of the list, effectively sorting the remaining elements around the even and odd numbers.
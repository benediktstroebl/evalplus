```python
def sort_third(lst):
    """This function sorts the list l such that values not divisible by three stay as they are, and are sorted as if they were divisible by three."""
    list_divisible_3 = [x for x in lst if x % 3 == 0]
    lst[:] = [x if x not in list_divisible_3 else lst.sort(list(lst))
    return lst
``` 
This function creates a list called `list_divisible_3` that contains all values in the list lst that are divisible by 3. Then, it sorts the list lst using the sort method.

It sorts the list in such a way that the values that are divisible by 3 are kept as they are and are sorted as if they were not divisible by three. The function then returns the list lst, which has been sorted as required.
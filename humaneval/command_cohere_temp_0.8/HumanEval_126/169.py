```python
def is_sorted(lst):
    # Count the unique elements and sort the list
    unique_count = len(set(lst))
    sorted_lst = sorted(lst)
    
    # If unique elements are greater than or equal to 2 and the list is sorted, return True
    if unique_count >= 2 and sorted_lst == lst:
        return True
    # Otherwise, return False
    else:
        return False
```

The `is_sorted` function takes a list of numbers `lst` as input and returns a boolean indicating whether the list is sorted in ascending order without duplicate values.

The approach is to:
1. Determine whether there's more than one unique element in the list. This is done using `len(set(lst))`, which counts unique elements and removes duplicates.
2. Sort the list (`sorted(lst)`), which will rearrange elements in ascending order.
3. Compare the sorted list to the original list: If they match, the list is both sorted and has no duplicates, so it's a valid scenario.
4. If these conditions are met, the function returns `True`; otherwise, it returns `False`. 

This algorithm is straightforward and efficient, guaranteeing correctness for the given scenarios.
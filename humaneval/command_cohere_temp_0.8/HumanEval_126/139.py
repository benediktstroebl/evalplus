```python
def is_sorted(lst):
    return all(e <= lst[i + 1] for i, e in enumerate(lst)) and len(set(lst)) == len(lst)
```
The function `is_sorted` checks two conditions to determine whether the list is sorted:
1. The list's elements are non-decreasing, verified by checking that each element is less than or equal to the next one (`all(e <= lst[i + 1] for i, e in enumerate(lst))`).
2. There are no duplicates in the list, confirmed by checking that the number of distinct elements in the list is equal to the length of the list (`len(set(lst)) == len(lst)`). 

This conditions allow the function to correctly determine whether the list is sorted while accounting for the constraint about duplicates.
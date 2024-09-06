```python
def is_sorted(lst):
    return all(e <= lst[i+1] for i, e in enumerate(lst)) and len(set(lst)) == len(lst)
```
The function leverages two conditions to determine whether the list is sorted:
1. All elements are less than or equal to the subsequent element in the list: This property of sorted lists is inferred using a generator expression, where each element is compared to the next one.
2. The list has unique elements: This condition is checked using `len(set(lst)) == len(lst)`, ensuring no duplicate values.

In this way, the function detects sorted and unique lists, returning `True`. If the list is not sorted or has duplicates, it returns `False`.
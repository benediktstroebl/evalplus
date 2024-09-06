```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` utilizes the Python built-in sorting mechanism `sort()` to arrange the elements of the input list in ascending order. Subsequently, it verifies the length of the list, returning `None` if the length is insufficient to capture the 2nd smallest element, which is determined by the condition `if len(lst) < 2`. In the case where the list length is at least 2, the function returns the 2nd smallest element, which is efficiently captured by indexing the sorted list at position 1, depicted as `else: return lst[1]`. 

This approach ensures not only accuracy but also efficiency in solving the given problem.
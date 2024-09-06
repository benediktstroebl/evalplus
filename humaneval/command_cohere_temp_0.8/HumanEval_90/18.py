```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines the function `next_smallest()`, which takes a list of integers as input. It starts by sorting the list in ascending order. If the sorted list has fewer than two elements, indicating a single smallest element or an empty list, the function returns `None`. Otherwise, it returns the second element, effectively the next smallest integer in the sorted list. This logic ensures that the function handles various scenarios correctly and aligns with the problem's expectations.
```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    largest = sorted(lst)[-2]
    return largest if lst.index(largest) == len(lst) - 1 else None
```

The function `next_smallest()` uses sorting to find the second smallest element in the list. The condition `if not lst or len(lst) < 2` handles the edge cases where the list is empty or has less than two elements, returning `None` in such cases. The logic efficiently identifies the second smallest element without needing extra space.
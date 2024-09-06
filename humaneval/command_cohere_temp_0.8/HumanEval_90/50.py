```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    ls = sorted(lst)
    return ls[1] if len(ls) >= 2 else None
```

The function `next_smallest()` uses sorting to determine the 2nd smallest number, returning `None` if the list has less than 2 elements. The unit tests demonstrate its usage and confirm its correctness against the provided scenarios.  This solution is efficient with a time complexity of O(N log N) due to the sorting step.
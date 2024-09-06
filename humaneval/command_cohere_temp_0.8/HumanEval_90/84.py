```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` utilizes the Python built-in sorting mechanism, `sort()`, to arrange the elements of the input list in ascending order. By doing this, the smallest element will be at the list's beginning, and the largest element will be at its end.

After sorting, the function verifies the length of the list. If it contains less than two elements, there is no second-smallest value, so the function returns `None`. However, if there are at least two elements, the function returns the second element, which is the second smallest due to the sorting that was previously performed.

This approach is efficient and works for all inputs as described in the problem statement.
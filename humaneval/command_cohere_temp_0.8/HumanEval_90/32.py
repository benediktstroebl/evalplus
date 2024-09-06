```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    mn = min(lst)
    ng = None
    for n in lst:
        if n > mn and (ng is None or n < ng):
            ng = n
    return ng
```
The function `next_smallest()` takes a list of integers as input and returns the second smallest element in the list. It handles cases with less than two elements correctly, returning `None` for a empty list and a list with only one element. It finds the smallest element through the use of `min()`, and then finds the element that is greater than the smallest element, but is the smallest among the remaining elements, using a loop and a potentially temporary variable `ng` to keep track of the second smallest element found so far.
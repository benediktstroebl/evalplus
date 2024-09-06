```python
def strange_sort_list(lst):
    result = []
    while len(lst) > 0:
        min_idx = result.index(min(result)) if len(result) > 0 else len(lst) - 1
        max_idx = result.index(max(lst)) if len(lst) > 0 else -1
        result.insert(min_idx, lst.pop(max_idx))
    return result
```

The code solves the problem using a `while` loop. It takes the `min` value from the `result` list or the `max` value from the `lst` list, whichever is available, and inserts it in the `result` list at the correct position. The `index` function returns the position of the `min` or `max` value for convenient picking of the next number to remove from the `lst` list. The loop continues until all numbers are processed.

The tests demonstrate the function with various input lists, including empty lists, and validate that the output list respects the strange sorting pattern.
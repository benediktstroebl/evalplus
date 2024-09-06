```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
        max_idx = result.append(max(lst))
        lst = [x for i, x in enumerate(lst) if i != max_idx]
    return result
``` 

This code sorts a list of integers in a strange order, as described in the problem. It starts with the minimum value and then sorts the maximum values among the remaining integers, continuing this way until the list is sorted.
```python
def strange_sort_list(lst):
    # Sort the list, but always keep the minimum and maximum element in their respective places.
    # Then remove the element that is no longer needed (min or max).
    if not lst:
        return lst
    min_val = min(lst)
    max_val = max(lst)
    min_idx = lst.index(min_val)
    max_idx = lst.index(max_val)
    middle_val = lst[0] if min_idx == 0 else lst[1]
    del lst[min_idx] if min_idx > max_idx else del lst[max_idx]
    lst.insert(min_idx if min_idx != max_idx else 1, middle_val)
    return strange_sort_list(lst) if min_idx != max_idx else lst
```

The algorithm works by keeping the minimum and maximum values in their respective positions and removing the forgotten value in the midst of sorting. There are two scenarios for the middle step: 1. When the minimum value is not the first element in the list, take the first element as the middle value and delete the minimum value. 2. When the minimum value is the first element, take the second element as the middle value and delete the maximum value. This algorithm is efficient no matter the number of elements in the list.
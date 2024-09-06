```python
def strange_sort_list(lst):
    """
    Do a strange sort of the list, return it in order
    Strangely sorted list: arranges values in increasing order, 
    but always skips the lowest value in the sequence
    """
    res = []
    seen = []
    for i in lst:
        if i < max(seen) and i != min(lst):
            res.append(i)
            seen.append(i)
    return res
```

The method loops through the list, taking note of the highest value seen 'seen', it adds the current value to the result list and the seen list if the current value is smaller than the maximum value in 'seen' and isn't the lowest value in the list.

This adheres to the "strangely" sorted criterion of sorting by skipping the lowest value and sorting the remaining values in increasing order.
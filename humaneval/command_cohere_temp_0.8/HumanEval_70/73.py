```python
def strange_sort_list(lst):
    result = []
    while lst:
        min_idx = result.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
        result.append(max(lst))
        lst = [x for x in lst if x != max(lst)]
    return result
```

The code initiates an empty result list onto which the sorted elements are appended. It then enters a loop where it calculates the index of the minimum value in the list and appends it to the result. Subsequently, the minimum value is removed from the list and this process is repeated until the input list is empty. Thus the output of the function is a list sorted in the desired 'strange' manner.
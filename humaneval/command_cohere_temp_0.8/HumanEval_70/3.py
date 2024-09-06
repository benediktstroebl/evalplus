```python
def strange_sort_list(lst):
    out = [min(lst)]
    for x in lst:
        if x > out[-1]:
            out.append(x)
    return out
```

The function `strange_sort_list` iterates through the list, tracking the maximum value seen so far in `out[-1]`. When it encounters an element greater than the maximum, it adds the element to the `out` list. This process results in a sorted list but with the largest element in its odd-position.
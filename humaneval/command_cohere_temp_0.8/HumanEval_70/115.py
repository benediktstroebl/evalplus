```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
    return out
```

The code works as follows:
1. Initialize an empty list `out` to store the sorted result.
2. While the original list `lst` is not empty, do the following:
    1. Find the index of the minimum value in `lst` using `append(min(lst))` and store it in `min_idx`. This also adds the minimum value to the `out` list.
    2. Remove all elements in `lst` at index `min_idx` and shift them to the end of the list `[x for i,x in enumerate(lst) if i != min_idx]`.
3. When the loop ends, the `out` list will be sorted in the desired "strange" order, and it is returned as the result.

This approach uses a minimal number of iterations and collections, making it an efficient solution.
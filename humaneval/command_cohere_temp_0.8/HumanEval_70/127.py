```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i, x in enumerate(lst) if i != min_idx]
        if not lst:
            break
    return out
```

The code works by repeatedly finding the minimum value in the list and adding it to the `out` array. The rest of the minimum values are removed from the `lst` variable. This process continues until `lst` becomes empty and provides the desired "strange" sort order.
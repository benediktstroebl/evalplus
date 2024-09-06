```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst)
        for i, num in enumerate(lst):
            if num < lst[min_idx]:
                min_idx = i
        out.append(lst.pop(min_idx))
        if len(lst) > 1:
            max_idx = len(lst)
            for i, num in enumerate(lst):
                if num > lst[max_idx]:
                    max_idx = i
            out.append(lst.pop(max_idx))
    return out
```

The algorithm sorts the list in a "strange" way as described in the problem statement. It starts by finding the minimum value in the list, then finds the maximum value in the list minus the minimum, and so on. The process is repeated until the list is sorted in this strange manner.
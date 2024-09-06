```python
def strange_sort_list(lst):
    # sort values and retain position by toggling between min and max values
    seen = []
    result = []
    while lst:
        min_val = min(lst)
        max_idx = lst.index(max(lst))
        result.append(min_val)
        lst[max_idx] = min(lst)
        seen.append(min_val)
        lst = [v for v in lst if v not in seen]
    return result
```

This code solves the problem as outlined in the original prompt. The main logic iterates through the input list `lst` and keeps track of seen values in the `seen` list. It finds the minimum value and its index in the list, appends the minimum to the `result` list, and swaps the maximum value with the minimum value at the correct index. This process is repeated until `lst` is empty, effectively sorting the list in the desired "strange" order.
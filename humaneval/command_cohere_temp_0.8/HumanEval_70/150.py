```python
def strange_sort_list(lst):
    # Sort the list, but always leave the first element untouched (the minimum)
    return [min(lst)] + [max(lst[:i] + lst[i+1:]) for i in range(len(lst))]
```
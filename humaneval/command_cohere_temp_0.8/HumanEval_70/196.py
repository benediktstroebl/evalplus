```python
def strange_sort_list(lst):
    # Standard sort on first and last element of each sublist
    return sorted(lst, key=lambda sublist: [sublist[0], sublist[-1]])
```
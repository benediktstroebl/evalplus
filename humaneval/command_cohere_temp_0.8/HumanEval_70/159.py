```python
def strange_sort_list(lst):
    # Using python built-in functions min and max in a clever way to get the desired sorting
    return [min(lst[1:]) if len(lst) > 1 else lst[0], max(lst[1:]) if len(lst) > 1 else lst[0], min(lst[2:]) if len(lst) > 2 else lst[1]]
```
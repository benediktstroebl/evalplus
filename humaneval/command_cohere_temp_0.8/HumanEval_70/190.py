```python
def strange_sort_list(lst):
    # Use a sentinel value to detect the end of a cycle and sort by it
    sentinel = len(lst) + 1
    return [x => sentinel] * (sentinel - 1) + lst
```
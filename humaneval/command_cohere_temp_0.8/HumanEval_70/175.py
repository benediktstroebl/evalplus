```python
def strange_sort_list(lst):
    # Create a copy of the list to avoid original modification
    result = lst.copy()
    result.sort(key=lambda x: [x in result[:-1], x in result[1:]])
    return result
```

The `strange_sort_list` function takes a list as input and sorts it using a custom sorting key. This key determines the order of elements based on their presence in the sorted and unsorted portions of the list. The resulting list is then returned as the output.
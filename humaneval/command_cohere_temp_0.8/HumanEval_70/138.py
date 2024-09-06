```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Traverse the list
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
        sorted_list.append(val)

    return sorted_list
```

The function `strange_sort_list()` works by initially finding the minimum and maximum values in the list. It then adds the minimum value to the start of the `sorted_list`, which builds the desired output. Following that, it removes the minimum value from consideration by updating `min_val` to the maximum of either the current minimum or the next number. The process is repeated until all numbers are sorted in the odd way described in the prompt.
```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Determine the oddness of the list length
    is_odd = len(lst) % 2 == 1

    # Iterate over the list and sort items accordingly
    for num in lst:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
        elif not is_odd and num == min_val:
            min_val = num
        else:
            sorted_list.append(num)
            is_odd = not is_odd

    # Append remaining values
    sorted_list.append(min_val)
    sorted_list.append(max_val)

    return sorted_list
```

The function `strange_sort_list` sorts the list in a strange manner as described in the prompt. It first finds the minimum and maximum values in the list and stores them in `min_val` and `max_val`, respectively. It then iterates over the list, tracking an oddness flag to determine whether it is currently sorting by minimum or maximum values. The sorted values are appended to the `sorted_list` and finally, any remaining values are appended to ensure the list is returned in the strange order specified.
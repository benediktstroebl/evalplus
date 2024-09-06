```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using max_val and even positions using min_val
    for val in lst:
        if len(sorted_list) % 2 == 0:
            if val < min_val:
                min_val = val
                sorted_list.append(min_val)
        else:
            if val > max_val:
                max_val = val
                sorted_list.append(max_val)
    
    return sorted_list
```

The function `strange_sort_list` first identifies the minimum and maximum values in the list, initially setting them to positive and negative infinity, respectively. It then alternates between appending the minimum and maximum values to the `sorted_list`, starting with the former. As a result, the odd positions are populated with the maximum values, while the even positions are populated with the minimum values, creating the desired "strange" order.
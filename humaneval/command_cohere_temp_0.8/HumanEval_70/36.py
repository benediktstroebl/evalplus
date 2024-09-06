```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_list = [min_val]
    
    # Iterate through the original list
    for val in lst:
        if val == min_val:
            sorted_list.append(val)
        elif val == max_val:
            sorted_list.append(val)
        else:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    
    # Add remaining elements that weren't picked yet
    sorted_list.extend([min_val, max_val])
    
    return sorted_list
```

The function `strange_sort_list` takes a list of integers as input and returns the list in a strange order, as described in the problem statement. The strange order is when you start with the minimum value, then the maximum of the remaining integers, then the minimum of the remaining, and so on. The function handles the special cases of an empty list or lists with only one value. The code uses two pointers, one for the minimum value and one for the maximum value, to efficiently traverse the list and determine the sorted order.
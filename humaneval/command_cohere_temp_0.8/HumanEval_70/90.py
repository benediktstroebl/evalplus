```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the output list with the initial min and max values
    out_list = [min_val, max_val]
    
    # Pop the minimum and maximum values from the original list
    # to ensure that they're not included in the output more than once
    while min_val in lst and max_val in lst:
        lst.remove(min_val)
        lst.remove(max_val)
        
        # Find the new minimum and maximum values
        min_val = min(lst)
        max_val = max(lst)
        
        # Append the new values to the output list
        out_list.extend([min_val, max_val])
    
    # Append any remaining values in the original list to the output list
    out_list.extend(lst)
    
    return out_list
```

The function `strange_sort_list` sorts a list of integers in a strange order, as described in the problem statement. It first finds the minimum and maximum values in the list, adds these to a new list (`out_list`), and then iteratively removes the minimum and maximum values from the original list while finding the new minimum and maximum values. These new values are added to the `out_list` in alternating order. Any remaining integers in the original list are appended to `out_list` after all the sorting steps. This results in a list sorted in the specified strange order.
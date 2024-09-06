def strange_sort_list(lst):
    # Initialize min and max values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the output list with the initial min and max values
    out_list = [min_val, max_val]
    
    # Pop the min and max values from the original list
    # and add the remaining values in the next iteration
    for val in lst:
        if val == min_val:
            min_val = max_val
        elif val == max_val:
            max_val = min_val
        else:
            out_list.append(val)
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
    
    # Add the final min and max values to the output list
    # (since they were not included in the previous loop)
    out_list.extend([min_val, max_val])
    
    return out_list
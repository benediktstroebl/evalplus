def strange_sort_list(lst):
    # Determine the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    # Continue building the result list by alternating min and max values
    for val in lst:
        if val == min_val:
            result.append(max_val)
        elif val == max_val:
            result.append(min_val)
        else:
            result.append(val)
    
    return result
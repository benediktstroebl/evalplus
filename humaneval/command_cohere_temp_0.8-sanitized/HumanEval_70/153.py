def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_list = [min_val]
    
    # Loop through the original list
    for val in lst:
        if val == min_val:
            sorted_list.append(max_val)
        elif val == max_val:
            sorted_list.append(min_val)
        else:
            sorted_list.append(val)
    
    return sorted_list
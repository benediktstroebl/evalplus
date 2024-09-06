def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_lst = [min_val]
    
    # Iterate through the original list
    for val in lst:
        if val == min_val:
            sorted_lst.append(val)
        elif val == max_val:
            sorted_lst.append(val)
        else:
            min_val = min(val, min_val)
            max_val = max(val, max_val)
    
    # Add the last occurrence of maximum and minimum values
    sorted_lst.append(max_val)
    sorted_lst.append(min_val)
    
    return sorted_lst
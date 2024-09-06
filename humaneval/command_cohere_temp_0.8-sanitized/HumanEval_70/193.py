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
            min_val = min(val, min_val)
            max_val = max(val, max_val)
    
    # Add the remaining values of the original list to the sorted list
    sorted_list.extend(lst[len(sorted_list):])
    
    return sorted_list
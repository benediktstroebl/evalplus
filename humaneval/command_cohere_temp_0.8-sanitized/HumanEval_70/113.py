def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    while len(lst) > 1:
        # Add the next smaller value (min) in the remaining list
        result.append(min(lst[2:]))
        # Remove the previous smaller value from the list
        lst.remove(min_val)
        # Update the min and max values for the remaining list
        min_val = min(lst)
        max_val = max(lst)
    
    # Add the final min value to the result if there are still elements in the list
    if len(lst) == 1:
        result.append(min_val)
    
    return result
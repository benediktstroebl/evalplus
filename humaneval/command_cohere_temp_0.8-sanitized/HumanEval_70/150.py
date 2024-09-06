def strange_sort_list(lst):
    # Initialize min and max values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    # Pop the min and max values from the original list
    # to ensure that they're not considered in the subsequent iterations
    lst.remove(min_val)
    lst.remove(max_val)
    
    while len(lst) > 1:
        # Calculate the next min and max values
        next_min = min(lst)
        next_max = max(lst)
        
        # Add the next min and max values to the result
        result.extend([next_min, next_max])
        
        # Remove the next min and max values from the original list
        lst.remove(next_min)
        lst.remove(next_max)
    
    # Add any remaining elements in the original list to the result
    result.extend(lst)
    
    return result
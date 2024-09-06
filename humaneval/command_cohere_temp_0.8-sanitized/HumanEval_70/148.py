def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    while len(lst) > 1:
        # Add the next smaller value (min) in the result list
        result.append(min(lst))
        # Remove the minimum value from the list (assuming it's not the last element)
        lst.remove(min_val)
        
        # Update the min and max values
        min_val = result[len(result) - 1]
        max_val = result[1]
        
        # Add the next larger value (max) in the result list
        result.append(max_val)
        # Remove the maximum value from the list (assuming it's not the last element)
        lst.remove(max_val)
    
    # Add the last remaining value in the list to the result
    result.append(max_val)
    
    return result
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the result list with the initial minimum value
    result = [min_]
    
    while lst:
        # Add the maximum value of the remaining list (excluding the just added min_)
        result.append(max(lst[:len(result)]))
        
        # Remove the minimum and maximum values from the list
        lst -= [min_, max_]
        
        # Update the minimum and maximum values
        min_, max_ = min(lst), max(lst)
    
    # Append the last maximum value to the result
    result.append(max_)
    
    return result
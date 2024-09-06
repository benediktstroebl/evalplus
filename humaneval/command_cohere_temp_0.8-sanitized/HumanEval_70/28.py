def strange_sort_list(lst):
    # Determine the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the output list with the initial minimum value
    sorted_list = [min_val]
    
    # Iterate through the original list
    for val in lst:
        # If the current value is smaller than the maximum found so far
        if val < max_val:
            # Add the current value to the output list
            sorted_list.append(val)
        else:
            # Replace the maximum value in the output list with the current value
            sorted_list.append(max_val)
            # Update the maximum value to the current value
            max_val = val
    
    # Add remaining maximum value to the output list
    sorted_list.append(max_val)
    
    return sorted_list
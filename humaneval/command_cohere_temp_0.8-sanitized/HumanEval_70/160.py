def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the output list with the initial min and max values
    out = [min_, max_]
    
    while lst:
        # Add the next min value to the output list
        out.append(min(lst))
        # Remove the maximum value from the remaining list
        lst = [x for x in lst if x != max_]
    
    # Add the remaining maximum value to the end of the output list
    out.append(max_)
    
    return out
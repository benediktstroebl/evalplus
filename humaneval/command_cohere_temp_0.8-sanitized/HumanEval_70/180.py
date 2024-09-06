def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        del lst[lst.index(min_val)]
        del lst[lst.index(max_val)]
        result.extend([min_val, max_val])
    
    return result
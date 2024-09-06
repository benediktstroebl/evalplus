def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum values
    # and even positions with minimum values
    for val in lst:
        if len(sorted_list) % 2 == 0:
            # If the list is even add the minimum value
            if val < min_val:
                min_val = val
                sorted_list.append(min_val)
        else:
            # If the list is odd add the maximum value
            if val > max_val:
                max_val = val
                sorted_list.append(max_val)
    
    return sorted_list
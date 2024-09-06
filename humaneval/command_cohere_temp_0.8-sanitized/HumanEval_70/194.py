def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Loop through each value in the list and update min_val and max_val accordingly
    for val in lst:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the value to the sorted_list if min_val equals max_val
        if min_val == max_val:
            sorted_list.append(val)
            min_val = float('inf')
            max_val = float('-inf')

    # Append remaining values in the list to sorted_list
    sorted_list.extend(min_val for _ in lst if _ != min_val)
    
    return sorted_list
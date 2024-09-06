def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd places with min value and even places with max value
    for val in lst:
        if len(sorted_list) % 2 == 0:
            if val < max_val:
                sorted_list.append(val)
                max_val = val
        else:
            if val > min_val:
                sorted_list.append(val)
                min_val = val

    return sorted_list
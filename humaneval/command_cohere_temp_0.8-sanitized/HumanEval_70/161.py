def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using max_val and even positions using min_val
    for val in lst:
        if len(sorted_list) % 2 == 0:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
            sorted_list.append(min_val)
        else:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
            sorted_list.append(max_val)

    return sorted_list
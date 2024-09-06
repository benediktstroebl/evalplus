def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using max_val and even positions using min_val
    for i in lst:
        if len(sorted_list) % 2 == 0:
            if i < min_val:
                min_val = i
            elif i > max_val:
                max_val = i
            sorted_list.append(min_val)
        else:
            if i < min_val:
                min_val = i
            elif i > max_val:
                max_val = i
            sorted_list.append(max_val)

    return sorted_list
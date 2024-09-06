def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the original list
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val

        # Append the current minimum or maximum value to the sorted list
        if len(sorted_list) < 1 or val == min_val:
            sorted_list.append(min_val)
        elif val == max_val:
            sorted_list.append(max_val)

    return sorted_list
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Ensure that empty lists return an empty list
    if not lst:
        return []

    for val in lst:
        # Update minimum and maximum values
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the value to the sorted list in the correct order
        if val == min_val:
            sorted_list.append(max_val)
        else:
            sorted_list.append(min_val)
    return sorted_list
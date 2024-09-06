def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Ensure that empty lists return an empty list
    if not lst:
        return []

    for val in lst:
        # Update min and max values
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the current maximum value to the sorted list
        sorted_list.append(max_val)

        # Swap maximum and minimum values for the next iteration
        max_val, min_val = min_val, max_val

    # Add the remaining maximum value to the sorted list
    sorted_list.append(max_val)

    return sorted_list
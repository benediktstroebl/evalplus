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
        else:
            continue

        # Append the current minimum or maximum value to the sorted list
        sorted_list.append(min_val if sorted_list else max_val)
        min_val = float('inf')
        max_val = float('-inf')

    # Append any remaining values to the sorted list
    sorted_list.append(min_val if sorted_list else max_val)

    return sorted_list
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

        # Append the current value to the sorted list
        sorted_list.append(val)

    # If the minimum value is greater than the maximum value, return the original list
    if min_val > max_val:
        return lst
    else:
        return sorted_list
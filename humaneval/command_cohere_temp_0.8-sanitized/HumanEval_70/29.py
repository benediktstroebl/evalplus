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

    # If the minimum value hasn't been added, add it to the end
    if min_val != float('inf'):
        sorted_list.append(min_val)

    # If the maximum value hasn't been added, add it to the beginning
    if max_val != float('-inf'):
        sorted_list.insert(0, max_val)

    return sorted_list
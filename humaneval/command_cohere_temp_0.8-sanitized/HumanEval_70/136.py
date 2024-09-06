def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for i in lst:
        if i > max_val:
            max_val = i
        elif i < min_val:
            min_val = i
        elif (len(sorted_list) + 1) % 2 == 0:  # Even position, add min_val
            sorted_list.append(min_val)
            min_val = float('inf')
        else:  # Odd position, add max_val
            sorted_list.append(max_val)
            max_val = float('-inf')

    # If the remaining maximum value is smaller than minimum value, add it to the sorted list.
    if max_val < min_val:
        sorted_list.append(max_val)

    return sorted_list
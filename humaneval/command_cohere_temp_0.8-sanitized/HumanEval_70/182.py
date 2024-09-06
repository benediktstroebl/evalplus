def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for i in lst:
        if i > max_val:
            max_val = i
            odd = True
        elif i < min_val:
            min_val = i
            odd = False
        elif odd is True:
            sorted_list.append(max_val)
            odd = False
        else:
            sorted_list.append(min_val)
        odd = not odd

    # Add the remaining maximum and minimum values to the end of the list.
    sorted_list.append(max_val)
    sorted_list.append(min_val)

    return sorted_list
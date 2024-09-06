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
        sorted_list.append(val)

    # If only one value was provided, return the list with only that value
    if len(sorted_list) == 1:
        return [max_val] * len(lst)

    return sorted_list
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with minimum values and even positions with maximum values
    for i, num in enumerate(lst):
        if i % 2 == 1:
            min_val = min(min_val, num)
        else:
            max_val = max(max_val, num)
        sorted_list.append(min_val if i % 2 == 1 else max_val)

    return sorted_list
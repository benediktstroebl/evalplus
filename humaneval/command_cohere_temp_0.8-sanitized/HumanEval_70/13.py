def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using maximum and even positions using minimum
    for i, num in enumerate(lst):
        if i % 2 == 0:
            # If even, add minimum (num) to sorted_list
            sorted_list.append(num)
            if num < min_val:
                min_val = num
        else:
            # If odd, add maximum to sorted_list
            sorted_list.append(max_val)
            if num > max_val:
                max_val = num

    return sorted_list
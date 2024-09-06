def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using maximum and even positions using minimum
    for i, num in enumerate(lst):
        if i % 2 == 0:
            # If the current number is greater than the minimum, update min_val and add the number to the result list
            if num >= min_val:
                min_val = num
                sorted_list.append(num)
        else:
            # If the current number is less than the maximum, update max_val and add the number to the result list
            if num <= max_val:
                max_val = num
                sorted_list.append(num)

    return sorted_list
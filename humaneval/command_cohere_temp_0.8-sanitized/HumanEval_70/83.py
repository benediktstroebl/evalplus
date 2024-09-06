def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for i, num in enumerate(lst):
        if i % 2 == 1:
            # Update max value if current number is greater than current max
            if num > max_val:
                max_val = num
        else:
            # Update min value if current number is smaller than current min
            if num < min_val:
                min_val = num
        # Populate the sorted list with the appropriate value based on the iteration type.
        sorted_list.append(num if i % 2 == 0 else max_val if max_val == num else min_val if min_val == num else num)
    return sorted_list
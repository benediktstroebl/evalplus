def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    lst_sorted = []

    # Determine the minimum and maximum values of the non-repeated numbers
    for num in lst:
        if num != lst[0]:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num

    # Append the unique min and max values to the sorted list
    lst_sorted.extend([min_val, max_val])

    # Sort the remaining elements of the list
    lst_sorted.extend(sorted(lst[1:], key=lambda x: [min_val, max_val].index(x)))

    return lst_sorted
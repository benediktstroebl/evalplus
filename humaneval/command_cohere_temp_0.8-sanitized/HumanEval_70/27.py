def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    lst_sorted = []

    # Ensure that empty lists return an empty list
    if not lst:
        return lst_sorted

    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

        # Append the current integer, or the minimum if max_val has not been updated yet
        lst_sorted.append(min(num, max_val))
        max_val = max(max_val, num)

    return lst_sorted
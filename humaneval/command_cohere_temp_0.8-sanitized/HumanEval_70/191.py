def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        list: List sorted in strange order.
    """
    # Check if the list is empty
    if not lst:
        return lst

    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    strange_sorted_list = [min_val]

    # Iterate through the original list
    for num in lst:
        # If the number is greater than the current maximum
        if num > max_val:
            strange_sorted_list.append(max_val)
            max_val = num
        # If the number is less than the current minimum
        elif num < min_val:
            strange_sorted_list.append(min_val)
            min_val = num

    # Append the last maximum value if it's greater than the minimum
    if max_val > min_val:
        strange_sorted_list.append(max_val)

    return strange_sorted_list
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
    result = [min_val]

    # Iterate over the remaining elements in the list
    for val in lst:
        if val == max_val:
            result.append(val)
        elif val < max_val:
            result.append(val)
        else:
            result.append(max_val)
            max_val = val

    return result
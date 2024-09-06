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

    # Initially sort the list with the smallest value in the first position.
    sorted_list = [min(lst)]

    # Remove the smallest value from the remaining list.
    lst = [x for x in lst if x > sorted_list[0]]

    # Repeat the process until the list is empty.
    while lst:
        # Put the maximum value of the remaining list in the next position.
        sorted_list.append(max(lst))
        lst = [x for x in lst if x < sorted_list[-1]]

    return sorted_list
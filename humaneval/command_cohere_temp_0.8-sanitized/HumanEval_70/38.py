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

    # Use the list to be sorted as a queue and use a set to track seen values
    queue = []
    seen = set()

    # Starting with the minimum value
    queue.append(min(lst))
    seen.add(min(lst))

    # Adding the maximum value of the remaining integers
    queue.append(max(filter(lambda x: x not in seen, lst)))
    seen.add(max(filter(lambda x: x not in seen, lst)))

    # Build the sorted list
    res = []
    while queue:
        # Add the minimum value of the current queue
        res.append(queue.pop(0))
        # Add the maximum value of the remaining queue
        res.append(queue.pop(0))

    return res
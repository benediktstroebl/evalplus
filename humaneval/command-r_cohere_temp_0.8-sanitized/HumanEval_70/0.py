def strange_sort_list(lst):
    '''
    Sort the list in a strange order.

    Args:
        lst (list): List of integers to be sorted.

    Returns:
        list: Sorted list in strange order.
    '''
    sorted_lst = []
    min_val = float('inf')

    # Find the minimum value in the list
    for num in lst:
        min_val = min(min_val, num)

    # Strange sorting
    while lst:
        sorted_lst.append(min_val)
        max_val = max(lst)
        lst.remove(max_val)
        min_val = min_val + 1

    return sorted_lst
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you reach the greatest integer in the list.

    Parameters:
        lst (list): List of integers.

    Returns:
        list: List sorted in the strange way described above.
    """
    if len(lst) <= 1:
        return lst
    return [min(lst)] + [max(lst[:-1])] + strange_sort_list(lst[:-1])
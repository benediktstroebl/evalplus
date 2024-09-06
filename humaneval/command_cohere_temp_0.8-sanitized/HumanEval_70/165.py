def strange_sort_list(lst):
    """
    Do a strange sort of a list, i.e., start with the smallest value,
    then the largest value among the remaining, then the smallest, and so on.

    Args:
        lst (list): List of integers

    Returns:
        list: Strangely sorted list
    """
    if len(lst) <= 1:
        return lst
    return [x for x in lst if lst.count(x) % 2 == 1 | lst.sort()]
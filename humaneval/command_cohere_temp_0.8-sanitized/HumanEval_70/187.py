def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting, is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you have passed through all the numbers.
    """
    if not lst:
        return lst
    return [min(lst[1:]) for _ in range(len(lst))] + strange_sort_list(lst[1:])
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you reach the maximum value in the list.
    """
    if not lst:
        return lst
    min_val = min(lst)
    max_remainder = max(lst[:-1])
    return [min_val] + [max_remainder] * (len(lst) - 2) + [max(lst)]
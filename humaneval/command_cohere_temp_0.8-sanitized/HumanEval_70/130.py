def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting, is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you have iterated through all the items.
    """
    if lst == []: 
        return []
    return [min(lst)] + [max(lst[:-1])] * (len(lst) - 2) + [min(lst[-1:])]
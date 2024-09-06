def strange_sort_list(lst):
    """
    Do a strange sort of the list, return it in order
    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining, then the minimum, and so on.
    """
    if len(lst) == 0:
        return lst
    return [min(lst[0:len(lst)//2])] + [max(lst[len(lst)//2+1:])]+ strange_sort_list(lst[len(lst)//2+1:])
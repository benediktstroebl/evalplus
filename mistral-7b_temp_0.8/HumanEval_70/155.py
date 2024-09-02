
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    #return sorted(lst)
    #return sorted(lst, reverse=True)
    #return sorted(lst)[::-1]
    #return [max(lst), min(lst[1:])] + strange_sort_list(lst[1:-1])
    #return [min(lst), max(lst[1:])] + strange_sort_list(lst[1:-1])

    if len(lst) == 0:
        return lst
    elif len(lst) == 1:
        return [lst[0]]

    #print(lst[0], max(lst[1:]), min(lst[1:]))
    return [lst[0]] + [max(lst[1:])] + strange_sort_list(lst[1:-1]) + [min(lst[1:])]

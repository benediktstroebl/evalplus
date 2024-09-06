
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
    strange_lst = []
    if not lst:
        return lst
    else:
        strange_lst.append(min(lst))
        lst.remove(min(lst))
        strange_lst.append(max(lst))
        lst.remove(max(lst))
        strange_lst.extend(lst)
    return strange_lst


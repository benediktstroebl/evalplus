
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
    if lst == []:
        return []
    else:
        minm = min(lst)
        lst.remove(minm)
        maxm = max(lst)
        lst.remove(maxm)
        strange_sort_list(lst)
        lst.append(minm)
        lst.append(maxm)
        lst.sort()
        return lst

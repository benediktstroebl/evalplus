
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
    if not lst:
        return lst
    min = min(lst)
    max = max(lst)
    if lst.count(min) == 1:
        lst.remove(min)
    if lst.count(max) == 1:
        lst.remove(max)
    lst.append(min)
    lst.append(max)
    return strange_sort_list(lst)


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
    if lst:
        m = lst[0]
        for i in range(len(lst)):
            if lst[i] < m:
                m = lst[i]
            elif lst[i] > m:
                lst.insert(i, lst.pop(i + 1))
                m = lst[i]
        return strange_sort_list(lst)
    else:
        return

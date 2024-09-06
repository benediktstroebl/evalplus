
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
        return lst
    lst2 = []
    mn = min(lst)
    lst.remove(mn)
    mx = max(lst)
    lst.remove(mx)
    lst2.append(mn)
    lst2.append(mx)
    for i in lst:
        lst2.append(i)
    return lst2

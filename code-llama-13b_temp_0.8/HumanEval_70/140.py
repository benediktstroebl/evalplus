
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
    lst_new = []
    n = len(lst)
    if n == 0:
        return lst_new
    lst.sort()
    for i in range(n):
        if i % 2 == 0:
            lst_new.append(lst[0])
            lst.remove(lst[0])
        else:
            lst_new.append(lst[-1])
            lst.remove(lst[-1])
    return lst_new


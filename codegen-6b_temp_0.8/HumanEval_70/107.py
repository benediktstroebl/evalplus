
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
    # l = len(lst)
    if not lst:
        return lst
    # for i in xrange(l):
    #     lst[i] = (i, lst[i])
    # lst.sort(key=lambda x: x[1])
    # return [i[0] for i in lst]
    n = len(lst)
    for i in xrange(n):
        lst[i] = (lst[i], -lst[i], i)
    lst.sort(key=lambda x: x[1])
    lst.sort(key=lambda x: x[2])
    return [i[0] for i in lst]


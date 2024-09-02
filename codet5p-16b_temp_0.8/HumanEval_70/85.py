
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

    lst.sort()
    print(lst)
    res = []
    i = 0
    while lst:
        res.append(lst.pop(i))
        if len(lst) >= 1:
            res.append(lst.pop(-i-1))
            i+=1
    return res




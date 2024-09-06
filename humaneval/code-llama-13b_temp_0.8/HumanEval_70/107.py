
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

    res = []
    flag = True
    while lst:
        if flag:
            mini = min(lst)
            res.append(mini)
            lst.remove(mini)
        else:
            maxi = max(lst)
            res.append(maxi)
            lst.remove(maxi)
        flag = not flag
    return res



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
    if len(lst) == 1:
        return lst
    res = []
    while lst:
        min = 10000
        for x in lst:
            if x < min:
                min = x
        res.append(min)
        lst.remove(min)
        max = -10000
        for x in lst:
            if x > max:
                max = x
        res.append(max)
        lst.remove(max)
    return res


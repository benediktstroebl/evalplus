
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
    temp = lst
    while len(temp) > 1:
        minimum = min(temp)
        maximum = max(temp)
        res.append(minimum)
        res.append(maximum)
        temp.remove(minimum)
        temp.remove(maximum)
    if len(temp) == 1:
        res.append(temp[0])
    return res

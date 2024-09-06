
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
        return []

    for index, item in enumerate(lst):
        if index == 0:
            minimum = item
            maximum = item
            continue
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item

    res = []

    while lst:
        if len(lst) == 1:
            res.append(lst[0])
            break
        if lst[0] == minimum:
            res.append(minimum)
            lst.pop(0)
            if not lst:
                break
            minimum = maximum
        if lst[0] == maximum:
            res.append(maximum)
            lst.pop(0)
            if not lst:
                break
            maximum = minimum
    return res

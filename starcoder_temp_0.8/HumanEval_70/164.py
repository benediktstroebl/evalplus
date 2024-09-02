
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

    res = []
    min_index = 0
    max_index = len(lst) - 1

    while len(res) < len(lst):
        res.append(lst[min_index])
        min_index += 1
        res.append(lst[max_index])
        max_index -= 1

    return res

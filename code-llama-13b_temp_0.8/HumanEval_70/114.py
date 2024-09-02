
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
    sorted_list = sorted(lst)
    res = []
    start_from_min = True
    while len(sorted_list) > 0:
        if start_from_min:
            res.append(sorted_list[0])
            del sorted_list[0]
        else:
            res.append(sorted_list[-1])
            del sorted_list[-1]
        start_from_min = not start_from_min
    return res
    

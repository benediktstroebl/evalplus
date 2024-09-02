
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

    if len(lst) == 0:
        return []
    minimum = min(lst)
    new_lst = []
    while len(lst) > 0:
        lst.remove(minimum)
        new_lst.append(minimum)
        if len(lst) == 0:
            break
        minimum = max(lst)
        lst.remove(max(lst))
        new_lst.append(max(lst))
    return new_lst


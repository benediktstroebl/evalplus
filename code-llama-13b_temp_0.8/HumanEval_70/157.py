
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

    new_list = []
    while len(lst) > 0:
        minimum = min(lst)
        new_list.append(minimum)
        lst.remove(minimum)
        if lst == []:
            return new_list
        maximum = max(lst)
        new_list.append(maximum)
        lst.remove(maximum)
        if lst == []:
            return new_list
    return new_list


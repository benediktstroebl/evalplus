
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
    lst = sorted(lst)
    new_list = []
    for i in range(len(lst)):
        if i == 0:
            new_list.append(lst[i])
            lst.pop(i)
        if i == len(lst) - 1:
            new_list.append(lst[i])
            lst.pop(i)
        if i == len(lst) - 1:
            new_list.append(lst[i])
            lst.pop(i)
        if i == len(lst) - 2:
            new_list.append(lst[i])
            lst.pop(i)
    return new_list


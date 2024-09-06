
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
        return lst
    new_list = []
    lst.sort()
    while len(lst) != 0:
        new_list.append(lst[0])
        lst.pop(0)
        if lst:
            lst.sort(reverse=True)
            new_list.append(lst[0])
            lst.pop(0)
    return new_list


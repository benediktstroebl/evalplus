
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

    new_lst = sorted(lst)
    strange_lst = [new_lst[0]]
    for i in new_lst:
        if strange_lst[-1] == i:
            strange_lst.append(i)
        else:
            strange_lst.append(i)
            strange_lst.append(i)
    return strange_lst

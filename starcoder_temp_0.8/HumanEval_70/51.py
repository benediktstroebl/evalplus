
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
    else:
        mini = lst[0]
        new_lst = []
        for i in lst:
            if i < mini:
                new_lst.append(i)
                new_lst.append(mini)
                mini = i
        new_lst.append(mini)
        return strange_sort_list(new_lst[len(new_lst) - len(lst) - 1:])

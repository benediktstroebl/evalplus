
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
    sorted_lst = []
    for i in lst:
        if len(sorted_lst) == 0:
            sorted_lst.append(i)
        elif i < sorted_lst[-1]:
            sorted_lst.append(i)
        else:
            sorted_lst.insert(0, i)
    return sorted_lst



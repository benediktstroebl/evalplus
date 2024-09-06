
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
    return_list = []
    for x in lst:
        if return_list == []:
            return_list.append(x)
        else:
            if x > return_list[-1]:
                return_list.append(x)
            else:
                return_list.insert(0, x)
    return return_list

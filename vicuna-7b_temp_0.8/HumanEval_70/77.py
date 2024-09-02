
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
    current_min = float('inf')
    for x in lst:
        if x < current_min:
            current_min = x
        elif x > current_min:
            sorted_lst.append(current_min)
            current_min = x
        else:
            sorted_lst.append(x)
    return sorted_lst

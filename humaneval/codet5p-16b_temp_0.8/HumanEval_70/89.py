
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

    min_lst = lst[0]
    max_lst = lst[0]
    sorted_lst = [min_lst]
    for i in range(1, len(lst)):
        if min_lst > lst[i]:
            min_lst = lst[i]
            sorted_lst.insert(0, min_lst)
        elif max_lst < lst[i]:
            max_lst = lst[i]
            sorted_lst.append(max_lst)
        else:
            sorted_lst.insert(0, lst[i])

    return sorted_lst

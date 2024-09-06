
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
    lst_copy = lst[:]
    lst_copy.sort(reverse=True)
    for i in range(len(lst_copy)):
        if lst_copy[i]!= i + 1:
            return lst_copy[i:] + [lst_copy[i]] + lst_copy[:i]
    return lst

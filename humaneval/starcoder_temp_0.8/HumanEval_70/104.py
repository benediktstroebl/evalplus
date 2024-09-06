
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
    if len(lst) <= 1:
        return lst
    min_ind = lst.index(min(lst))
    max_ind = lst.index(max(lst[min_ind+1:])) + min_ind + 1
    return (lst[max_ind:] + lst[min_ind:max_ind] + lst[:min_ind] + lst[max_ind+1:])

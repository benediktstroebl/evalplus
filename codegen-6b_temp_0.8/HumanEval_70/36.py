
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
    lst = list(lst)
    lst.sort()
    min_index = lst.index(min(lst))
    lst[min_index], lst[-1] = lst[-1], lst[min_index]
    max_index = lst.index(max(lst))
    lst[max_index], lst[0] = lst[0], lst[max_index]
    return lst


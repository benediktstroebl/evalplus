
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
    if not lst:
        return lst
    min_value = min(lst)
    max_value = max(lst)
    middle = lst[lst.index(min_value):lst.index(max_value)+1]
    new_middle = middle[::-1]
    lst = lst[:lst.index(min_value)] + new_middle + lst[lst.index(max_value)+1:]
    return lst

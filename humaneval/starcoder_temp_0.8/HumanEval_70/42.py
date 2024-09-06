
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

    if len(lst) == 0:
        return lst
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return lst
        return [lst[1], lst[0]]
    smallest = min(lst)
    rest = lst[1:].copy()
    rest.remove(smallest)
    strange_rest = strange_sort_list(rest)
    strange_rest.append(smallest)
    return strange_rest
